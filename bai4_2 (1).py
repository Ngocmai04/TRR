# import heapq
#
# # Step 1: Read the words from the file and store them in a list
# with open('sgb-words.txt', 'r') as f:
#     word_list = [word.strip() for word in f]
#
# # Step 2: Create a dictionary that maps suffixes to words
# suffix_dict = {}
# for word in word_list:
#     for i in range(len(word) - 3):
#         suffix = word[i + 1:]
#         if suffix not in suffix_dict:
#             suffix_dict[suffix] = [word]
#         else:
#             suffix_dict[suffix].append(word)
#
# # Step 3: Create the directed graph D
# D = {word: [] for word in word_list}
# for word in word_list:
#     for i in range(len(word) - 3):
#         suffix = word[i + 1:]
#         for neighbor in suffix_dict[suffix]:
#             if neighbor != word:
#                 D[word].append((neighbor, 1))
#
# print('herh')


# Step 4: Use Dijkstra's algorithm to find the shortest path from u to v
def dfs(graph, start, visited, stack):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(start)


def get_transpose_graph(graph):
    transpose_graph = {node: set() for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            transpose_graph[neighbor].add(node)
    return transpose_graph


def kosaraju(graph):
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
    transpose_graph = get_transpose_graph(graph)
    visited = set()
    num_strongly_connected_components = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            dfs(transpose_graph, node, visited, [])
            num_strongly_connected_components += 1
    return num_strongly_connected_components


with open('sgb-words.txt', 'r') as f:
    words = [line.strip() for line in f]

graph = {word: set() for word in words}
for i, word1 in enumerate(words):
    for word2 in words[i + 1:]:
        if word1[-4:] in word2:
            graph[word1].add(word2)

num_strongly_connected_components = kosaraju(graph)
print("Number of strongly connected components:", num_strongly_connected_components)
