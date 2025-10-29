import sys
import urllib.request
from typing import Optional, List


class Node:
    def __init__(self, word: str):
        self.word = word
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

class BST:
    def __init__(self, source: str, **kwargs):
        self.root: Optional[Node] = None
        self.results: List[str] = []
        
        wordlist = self._load_wordlist(source, **kwargs)
        
        if wordlist:
            sorted_words = sorted(list(set(wordlist)))
            self.root = self._build_balanced_bst_recursive(sorted_words, 0, len(sorted_words) - 1)

    def _load_wordlist(self, source: str, **kwargs) -> List[str]:
        wordlist = []
        is_url = kwargs.get("url", False)
        
        if is_url:
                with urllib.request.urlopen(source) as response:
                    data = response.read()
                    text = data.decode("utf-8")
                    wordlist = [line.strip().lower() for line in text.splitlines() if line.strip()]
        else:
                with open(source, "r", encoding="utf-8") as f:
                    wordlist = [line.strip().lower() for line in f if line.strip()]
                    
       
            
        return wordlist

    def _build_balanced_bst_recursive(self, words: List[str], start: int, end: int) -> Optional[Node]:
        if start > end:
            return None
            
        mid = (start + end) // 2
        
        node = Node(words[mid])
        node.left = self._build_balanced_bst_recursive(words, start, mid - 1)
        node.right = self._build_balanced_bst_recursive(words, mid + 1, end)
        
        return node

    def autocomplete(self, prefix: str) -> List[str]:
        self.results = []
        prefix_lower = prefix.lower()
        
        if self.root:
            self._collect(self.root, prefix_lower)
            
        return self.results

    def _collect(self, node: Optional[Node], prefix: str):
        if node is None:
            return

        if node.word.startswith(prefix):
            self._collect(node.left, prefix)
            self.results.append(node.word)
            self._collect(node.right, prefix)
        elif prefix < node.word:
            self._collect(node.left, prefix)
        else:
            self._collect(node.right, prefix)