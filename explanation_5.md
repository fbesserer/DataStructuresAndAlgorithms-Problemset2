### Design decision
The implemented AutoCompleteTrie has the following time complexities:
- Trie.insert(): O(m) with m being the amount of characters in the word 
- Trie.find(): O(m) with m being the amount of characters in prefix
- TrieNode.suffixes(): O(m) - every note is visited once

The implemented RouterTrie has the following space complexities:
- Trie.insert(): O(n)
- Trie.find(): O(n) 
- TrieNode.suffixes(): O(n) 

with n being the number of nodes in the trie

An overall space complexity of O(n) with n being the nodes in the trie can be expected in an implementation 
with a hashtable.