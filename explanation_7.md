### Design decision
The implemented RouterTrie has the following time complexities:
- RouteTrie.insert(): O(m)
- RouteTrie.find(): O(m) - finding each word in a dict takes O(1)  
- Router.split_path(): O(m + d) with d being the characters in the path regarding the inbuilt split() method
- Router.add_handler(): O(2m + d) considering that split_path() and RouteTrie.insert() are part of the function
- Router.lookup(): O(2m + d) considering that split_path() and RouteTrie.find() are part of the function

with m being the length of the given path split on the slashes "/" eg the number of individual words.

The implemented RouterTrie has the following space complexities:
- RouteTrie.insert(): O(n)
- RouteTrie.find(): O(1)
- Router.split_path(): O(2m*d) or O(2n) - two lists are created by split() and list comprehension  
- Router.add_handler(): O(3n) - combination of insert and split_path
- Router.lookup(): O(2n)

with n being the characters of the path to be saved.

An overall space complexity of O(n) with n being the length of all strings for storing all entries can be expected in an implementation 
with a hashtable.