
from collections import defaultdict
from graph import Graph
# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)
# def dfs(starting_vertex, family):
#     """
#     Return a list containing a path from
#     starting_vertex to destination_vertex in
#     depth-first order.
#     """
#     s = Stack()
#     s.push([starting_vertex])
#     visited = []
#     while s.size() > 0:
#         current_path = s.pop()
#         last_vertex = current_path[-1]
#         if last_vertex not in family:
#             family[last_vertex] = []
#         if last_vertex not in visited:
#             visited.append(last_vertex)
#         for child in family[last_vertex]:
#             new_path = current_path[:]
#             new_path.append(child)
#             s.push(new_path)
#     return visited[-1]
   

def earliest_ancestor(ancestors, starting_node):
    # ancestors is an array of parent child pairs 1 is parent of 3 (1, 3)
    # example input [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1
    # example output 10, the parent of 1 is 10, 3 is a child of 2 and 10 but 10 is the furthest away from the child
    # Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor
    # – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
    # If the input individual has no parents, the function should return -1.

    #     '''
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # '''
    # start with 10, which has no parents as a base case.
    # Clarifications:
    # * The input will not be empty.
    # * There are no cycles in the input.
    # * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    # * IDs will always be positive integers.
    # * A parent may have any number of children.
    # family = {}
    # for parent, child in ancestors:
    #     family.setdefault(child, list()).append(parent)
    # if starting_node not in family:
    #     return -1   
    # earliest = dfs(starting_node, family)
    # return earliest
    g = Graph()
    longest_path = []
    for parent, child in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)
        g.add_edge(parent, child)
    for vertices in g.vertices:
        path = g.bfs(vertices, starting_node)
        if vertices != starting_node:
            if path is not None:
                if len(longest_path) < len(path):  
                    longest_path = path
                elif len(longest_path) == len(path) :
                    if longest_path[0] > path[0]:
                        longest_path = path
    if len(longest_path) == 0:
        return -1
    return longest_path[0]
    






test = earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 1)
print(test)