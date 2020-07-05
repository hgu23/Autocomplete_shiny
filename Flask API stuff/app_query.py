from flask import Flask, request
import tries_Harshil 
from tries_Harshil import Trie
from tries_Harshil import TrieNode
import autocomplete2
from autocomplete2 import helpers
import json
from gensim.utils import simple_preprocess as pre_process
from nltk import word_tokenize 
from nltk.util import ngrams
from nltk.tokenize.treebank import TreebankWordDetokenizer
import fse
from fse.models import Average
from fse import IndexedList
from gensim.models import FastText
from collections import Counter
import flask_cors
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, resources={r"/app_query/*": {"origins": "*"}})
query_list = open("/Users/harshitg/github/autocomplete/autocomplete/everything_combined_processed.txt").readlines()
keys = query_list
counter = Counter(keys)
trie = Trie() 
trie.formTrie(query_list) 
sentence_model = fse.models.SentenceVectors.load("/Users/harshitg/github/autocomplete/autocomplete/sentence2vec_everything_combined_word2vec_usif.model")
@app.route('/',methods = ['GET','POST'])
def print_suggestions():
    if request.method == 'POST':
        auto_suggestions = trie.printAutoSuggestions(request.get_json().get('item'),query_list,10)
        if auto_suggestions == 0 or auto_suggestions == -1:
            trie.insert(request.get_json().get('item'))
            query_list.append(request.get_json().get('item'))
            auto_suggestions = "No autocomplete suggestions found for this prefix"
            semantic_suggestions_new2 = []
        elif query_list.index(auto_suggestions[0]) < len(sentence_model): 
            semantic_suggestions = sentence_model.most_similar(query_list.index(auto_suggestions[0]), topn=counter[auto_suggestions[0]]+10)
            semantic_suggestions_new = semantic_suggestions[counter[auto_suggestions[0]]-1:len( semantic_suggestions)]
            semantic_suggestions_new2 = []
            for i in range(0,len(semantic_suggestions_new)):
                suggestion = query_list[semantic_suggestions_new[i][0]]
                semantic_suggestions_new2.append(suggestion)
        else:
            semantic_suggestions_new2 = []
        return json.dumps([auto_suggestions,semantic_suggestions_new2])

