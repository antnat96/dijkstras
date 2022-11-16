# Author: Anthony Natale
# Date: Nov 2022
# CSCI 6410 Assignment 5
# Instructions:
# 1. Run 'python main.py' without the quotes.
# 2. When prompted to input, paste the entire graph representation OR enter it line by line, and when finished hit
#    enter TWICE to create an empty line. The program recognizes an empty line as the end of the input.
import math

# Heap helper functions
def parent(index):
    return index / 2

def ltChild(index):
    return (2 * index) + 1

def rtChild(index):
    return (2 * index) + 2


# Heap class
class Heap:
    def __init__(self, size):
        self.heap = [0] * size
        self.heap[0] = -1
        self.size = 0
        self.max_size = size

    def is_empty(self):
        return self.size == 0 or len(self.heap) == 0

    def leaf(self, index):
        return index > (self.size / 2) - 1

    def heapify(self, index):
        if self.leaf(index):
            return
        # TODO: Left off here

    # Swap two vertices in the heap
    def swap(self, first_index, second_index):
        temp = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp

    def insert(self, vertex):
        if self.size >= self.max_size:
            return

        self.size += 1
        self.heap[self.size] = vertex
        cur = self.size

        while self.heap[cur] < self.heap[parent(cur)]:
            self.swap(cur, parent(cur))
            cur = parent(cur)

    def extract_min(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.heapify(0)
        return minimum

    def show(self):
        print(self.heap)


def dijkstra(vertices, edges, adjacency_list, source):
    dist = [None] * len(vertices)
    prev = [None] * len(vertices)
    dist[source] = 0
    # Queue/Heap is set of all vertices in graph
    h = Heap(len(vertices))

    # Build the heap
    for v in vertices:
        h.insert(v)

    h.show()

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
