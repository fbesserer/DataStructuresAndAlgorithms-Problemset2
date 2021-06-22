'''
Autocomplete words using a trie
'''

# Represents a single node in the Trie
class TrieNode:
    suffix_list = []

    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        pass

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        if self.is_word and suffix != '': # fertige Wörter werden mit suffix != '' rausgefiltert dh nicht noch vorgeschlagen
            TrieNode.suffix_list.append(suffix)
        if self.children == {}:
            return TrieNode.suffix_list

        key = [key for key in self.children.keys()]
        for i in key:
            new_suffix = suffix + i
            # self.children[new_suffix[-1]].suffixes(new_suffix)
            self.children[i].suffixes(new_suffix)
        return TrieNode.suffix_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

find = MyTrie.find("trig")
if find:
    print(find.suffixes())
else:
    print("word not in dictionary")

