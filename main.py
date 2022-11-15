# Author: Anthony Natale
# Date: Nov 2022
# CSCI 6410 Assignment 5
# Instructions:
# 1. Run 'python main.py' without the quotes.
# 2. When prompted to input, paste the entire graph representation OR enter it line by line, and when finished hit
#    enter TWICE to create an empty line. The program recognizes an empty line as the end of the input.

class Heap:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0 or len(self.items) == 0


def dijkstra(vertices, edges, adjacency_list, source):
    dist = [None] * len(vertices)
    prev = [None] * len(vertices)
    dist[source] = 0
    # Queue/Heap is set of all nodes in graph
    h = Heap()

    while h.is_empty() is False:
        # u is node in q with smallest dist
        # remove u from heap
        # for each neighbor v of u:
        # alt = dist[u] + dist_between(u, v)
        # if alt < dist[v]:
        # dist[v] = alt
        # prev[v] = u
        pass

    return prev


def main():
    edges = []
    vertices = set()
    n = None
    e = None
    print('Enter the graph representation. When you are finished, enter an empty line and your input will be processed')

    while True:
        try:
            line = raw_input()
            # Exit on an empty line
            if line is None or line == "":
                raise EOFError
            # Remove new lines
            if "\n" in line:
                line = line.replace("\n", "")
            # First input line is number of vertices
            if n is None:
                n = int(line)
            # Second input line is number of edges
            elif e is None:
                e = int(line)
            # Further lines are edges and weights
            else:
                stripped_line = line.strip()
                split_line = stripped_line.split(" ")
                edge_1 = int(split_line[0])
                edge_2 = int(split_line[1])
                weight = int(split_line[2])
                edges.append([edge_1, edge_2, weight])
                vertices.add(edge_1)
                vertices.add(edge_2)
        except EOFError:
            break

    if e != len(edges):
        print('You may be missing an edge or may have entered extra edges. Please check your input.')

    # Create graph representation and initialize visited list
    adjacency_list = [None] * n
    for edge in edges:
        if adjacency_list[edge[0]] is None:
            adjacency_list[edge[0]] = [[edge[1], edge[2]]]
        else:
            adjacency_list[edge[0]].append([edge[1], edge[2]])

    print (adjacency_list)
    print(edges)
    print(vertices)

    print(dijkstra(vertices, edges, adjacency_list, 1))


if __name__ == '__main__':
    main()
