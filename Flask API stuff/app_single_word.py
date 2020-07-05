from flask import Flask, request
import tries_Harshil 
from tries_Harshil import Trie
from tries_Harshil import TrieNode
import autocomplete2
from autocomplete2 import helpers
import json
from gensim.models import Word2Vec
from collections import Counter
app = Flask(__name__)
huge_file = "/Users/harshitg/github/autocomplete/autocomplete/everything_combined_single.txt"
huge_list = []
with open(huge_file, "r") as f:
    for line in f:
        huge_list.extend(line.split())
keys = huge_list
counter = Counter(keys)
trie = Trie()
trie.formTrie(keys)
model = Word2Vec.load("/Users/harshitg/github/autocomplete/autocomplete/word2vec_all_cb.model")
model_vectors = model.wv       
@app.route('/',methods = ['GET','POST'])
def print_suggestions():
    if request.method == 'POST':
        auto_suggestions =  trie.printAutoSuggestions(request.get_json().get('item'),huge_list,10)
        if auto_suggestions  == 0 or auto_suggestions == -1: 
            auto_suggestions = ["No term found with this prefix\n"]
            trie.insert(request.get_json().get('item'))
            huge_list.append(request.get_json().get('item'))
            semantic_suggestions_new = [] 
            return json.dumps([auto_suggestions , semantic_suggestions_new])
        elif auto_suggestions[0] in model_vectors:
            semantic_suggestions = model.most_similar(positive= auto_suggestions[0], topn=10)
            semantic_suggestions_new = []
            for i in range(0,len(semantic_suggestions)):
                suggestion = semantic_suggestions[i][0]
                semantic_suggestions_new.append(suggestion)
            return json.dumps([auto_suggestions,semantic_suggestions_new])
        else:
            semantic_suggestions_new = []
            return json.dumps([auto_suggestions,semantic_suggestions_new])
