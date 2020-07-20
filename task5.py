class TrieNode:
    def __init__(self, end_of_word=False):
              self.end_of_word = end_of_word

        self.char_dict = dict()

    def insert(self, char):
         sub_char_node = TrieNode()
        self.char_dict[char] = sub_char_node

        return sub_char_node

    def suffixes(self, suffix=''):
    output_str_list = list()

        def find_suffix(node, output_str):

            # If end_of_word at this node is true, then add the suffix to result list
            if node.end_of_word:
                output_str_list.append(output_str)

            for char in node.char_dict:
                temp_output_str = output_str + char
                find_suffix(node.char_dict[char], temp_output_str)

        find_suffix(self, "")

        return output_str_list



class Trie:
    def __init__(self):
       
        root_node = TrieNode()
        self.root = root_node

    def insert(self, word):
        cur_node = self.root

        for char in word:
            if char in cur_node.char_dict:
                cur_node = cur_node.char_dict[char]
            else:
                new_child_node = cur_node.insert(char)
                cur_node = new_child_node

       
        cur_node.end_of_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix

        cur_node = self.root
        # Traverse the Trie tree base on the character sequence.
        for char in prefix:
            if char in cur_node.char_dict:
                cur_node = cur_node.char_dict[char]
            else:
                return None

        return cur_node

    def __str__(self):
        output_str = [""]

        def print_node(node, output_str):
            output_str[0] += f"\nEnd of word: {node.end_of_word}\n"
            for char in node.char_dict:
                output_str[0] += f"char: {char}"
                print_node(node.char_dict[char], output_str)

        print_node(self.root, output_str)

        return output_str[0]


MyTrie = Trie()
wordList = [
    "ant", "anthropology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

node = MyTrie.find('f')
print(node.suffixes())
