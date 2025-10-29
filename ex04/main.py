import sys
from bst import BST
from search_engine import search_loop

WORDLIST_SOURCE = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

def main():
 

    bst_engine = BST(WORDLIST_SOURCE, url=True)    
    search_loop(bst_engine.autocomplete)

if __name__ == "__main__":
    main()