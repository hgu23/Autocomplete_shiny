from flask import Flask, request
import tries_Harshil 
from tries_Harshil import Trie
from tries_Harshil import TrieNode
import autocomplete2
from autocomplete2 import helpers
import json
from gensim.models import Word2Vec
app = Flask(__name__)
huge_file = "/Users/harshitg/github/autocomplete/autocomplete/everything_combined_processed.txt"
huge_list = []
with open(huge_file, "r") as f:
    for line in f:
        huge_list.extend(line.split())
keys = list(helpers.chunks(huge_list,2)) # keys to form the trie structure. 
new_list = []
model = Word2Vec.load("/Users/harshitg/github/autocomplete/autocomplete/bigrams_fasttext_processed_cb.model")
model_vectors = model.wv 
for i in range(0,len(keys)):
    curr_list = keys[i]
    new_list.append(curr_list[0]+ ' ' + curr_list[1])
trie = Trie() 
trie.formTrie(new_list)   

@app.route('/',methods = ['GET','POST'])
def print_suggestions():
    if request.method == 'POST':
        auto_suggestions = trie.printAutoSuggestions(request.get_json().get('item'),new_list,10)
        if auto_suggestions == 0 or auto_suggestions == -1:
                trie.insert(request.get_json().get('item'))
                new_list.append(request.get_json().get('item'))
                auto_suggestions = ["No autocomplete suggestions with this prefix"]
                semantic_suggestions_new = []
        else:
            top = auto_suggestions[0]
            print(top)
            bigram = top.replace(" ","_")
            print(bigram)
            if bigram in model_vectors:
                semantic_suggestions = model.most_similar(positive=[bigram], topn=10)
                semantic_suggestions_new = []
                for i in range(0,len(semantic_suggestions)):
                    suggestion = semantic_suggestions[i][0]
                    new_suggestion = suggestion.replace("_"," ")
                    semantic_suggestions_new.append(new_suggestion)
            else:
                semantic_suggestions_new = [] 
        return json.dumps([auto_suggestions,semantic_suggestions_new])

