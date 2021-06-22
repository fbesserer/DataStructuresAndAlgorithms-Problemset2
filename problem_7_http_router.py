class RouteTrie:
    def __init__(self, handler, not_handler):
        self.root = RouteTrieNode()
        self.root.children["/"] = RouteTrieNode(handler)
        self.not_found_handler = not_handler

    def insert(self, path, handler):  # O(m) with m := number of path parts
        current_node = self.root.children["/"]
        for idx, part in enumerate(path):
            if part not in current_node.children:
                if idx == len(path) - 1:
                    current_node.children[part] = RouteTrieNode(handler)
                else:
                    current_node.children[part] = RouteTrieNode(self.not_found_handler)
            elif idx == len(path) -1:  # handles the case when a parent website is later added as a handle | removes the not_handle
                current_node.children[part].handler = handler
            current_node = current_node.children[part]

    def find(self, path):  # O(m) with m := number of path parts
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[part]
        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler


class Router:
    def __init__(self, handler, not_handler):
        self.trie = RouteTrie(handler, not_handler)

    def add_handler(self, path, handler):  # O(2m + d) with m := number of path parts
        parts = self.split_path(path)
        self.trie.insert(parts, handler)

    def lookup(self, path): # O(2m + d) with m := number of path parts
        parts = self.split_path(path)
        parts.insert(0, "/")
        return self.trie.find(parts)

    def split_path(self, path):  # O(m + d) with m := number of path parts, d:= digits in string "path"
        parts = [word for word in path.split("/") if word != ""]
        return parts


# test cases and expected outputs
router = Router("root handler", "the page has not been found")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/blog/057852/ComputerScience", "cs handler")  # add a route
router.add_handler("/home/blog/", "blog handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # 'root handler'
print(router.lookup("/home"))  # not_handler
print(router.lookup("/home/"))  # not_handler
print(router.lookup("/home/about"))  # 'about handler'
print(router.lookup("/home/about/"))  # 'about handler'
print(router.lookup("/home/about/me"))  # not_handler
print(router.lookup("/home/blog"))  # 'blog handler'
print(router.lookup("/home/blog/057852/ComputerScience"))  # 'cs handler'
print(router.lookup("/home/blog/057852/"))  # not_handler

