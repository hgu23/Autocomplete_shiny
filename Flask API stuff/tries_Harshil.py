from collections import Counter
import operator 
import pickle 
import sys
sys.setrecursionlimit(15000)
class TrieNode(): 
    def __init__(self): 
          
        # Initialising one node for trie 
        self.children = {} 
        self.last = False
  
class Trie(): 
    def __init__(self): 
          
        # Initialising the trie structure. 
        self.root = TrieNode() 
        self.word_list = [] 
  
    def formTrie(self, keys): 
          
        # Forms a trie structure with the given set of strings 
        # if it does not exists already else it merges the key 
        # into it by extending the structure as required 
        for key in keys: 
            self.insert(key) # inserting one key to the trie. 
  
    def insert(self, key): 
          
        # Inserts a key into trie if it does not exist already. 
        # And if the key is a prefix of the trie node, just  
        # marks it as leaf node. 
        node = self.root 
        for a in list(key): 
        ### If the letter of the prefix is not found in the child nodes, add them to the trie ##
            if not node.children.get(a): 
                node.children[a] = TrieNode() 
            node = node.children[a] 
        node.last = True
  
    def search(self, key): 
          
        # Searches the given key in trie for a full match 
        # and returns True on success else returns False. 
        node = self.root 
        found = True
  
        for a in list(key): 
            if not node.children.get(a):  ### If the key is not found in the child nodes,  breaks the loop. 
                found = False
                break
  
            node = node.children[a]  ### Creates a new node with the letter not found in the child nodes.###
  
        return node and node.last and found 
  
    def suggestionsRec(self, node, word): 
          
        # Method to recursively traverse the trie 
        # and return a whole word.  
        if node.last: 
            self.word_list.append(word) 
        ## Add characters to the word in word list as found in the child nodes ###
        for a,n in node.children.items(): 
            self.suggestionsRec(n, word + a) ##### Adds the letters in the child nodes of the current node (node corresponding to the 
                                             #####last letter of the prefix) to the prefix and then appends it into the 
                                             ##### list of suggestions) ####
    
    def printAutoSuggestions(self, key,WORDS,top_n): 
          
        # Returns all the words in the trie whose common 
        # prefix is the given key thus listing out all  
        # the suggestions for autocomplete. 
        self.word_list = []
        node = self.root 
        not_found = False
        temp_word = '' 
  
        for a in list(key): 
           ### If the key is not found in the children, break the loop ###
            if not node.children.get(a): 
                not_found = True
                break
           ### Add the keys to the temp_word string to form the prefix to be searched ###
            temp_word += a 
            ### Call the node corresponding to the current letter of the prefix if the character exists in the child nodes ###
            node = node.children[a] 
        self.suggestionsRec(node, temp_word)
        if not_found: 
            return 0
        elif node.last and not node.children: ### If the current node itself is the root node (no characters have been added to the trie 
            return -1                         ##structure)##
        freq_dict  = Counter(WORDS)
        dict = {}
        for s in self.word_list:
            dict[s] = freq_dict[s]
        sorted_tup = sorted(dict.items(), key=operator.itemgetter(1),reverse = True)
        sorted_list = []
        for tup in sorted_tup[:top_n]:
            sorted_list.append(tup[0])
        return sorted_list
    
