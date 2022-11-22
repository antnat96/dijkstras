# Author: Anthony Natale
# Date: Nov 2022
# CSCI 6410 Assignment 5
# Instructions:
# 1. Run 'python main.py' without the quotes.
# 2. When prompted to input, paste the entire graph representation OR enter it line by line, and when finished hit
#    enter TWICE to create an empty line. The program recognizes an empty line as the end of the input.
import math
import sys


# Heap helper functions
def parent(index):
    return (index - 1) // 2


def ltChild(index):
    return (2 * index) + 1


def rtChild(index):
    return (2 * index) + 2


# Heap class
class Heap:
    def __init__(self, max_size):
        # The heap
        self.heap = [None] * max_size
        # An array to watch/manage the position of a given vertex in the heap
        self.positions = [None] * max_size
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0 or len(self.heap) == 0

    def leaf(self, index):
        return index > (self.size / 2) - 1

    def heapify(self, index):
        if self.leaf(index):
            return
        temp_pos = index
        if rtChild(index) <= self.size:
            temp_pos = ltChild(index) if self.heap[ltChild(index)] < self.heap[rtChild(index)] else rtChild(index)
        else:
            temp_pos = self.heap[ltChild(index)]

        if self.heap[index] > self.heap[ltChild(index)] or self.heap[index] > self.heap[rtChild(index)]:
            self.swap(index, temp_pos)
            self.heapify(temp_pos)

    # Swap two vertices in the heap
    def swap(self, first_index, second_index):
        temp = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp

    def insert(self, vertex):
        if self.size >= self.max_size:
            return

        self.heap[self.size] = vertex
        self.positions[self.size] = vertex[0]
        self.size += 1
        #
        # next_vertex_index = self.size
        #
        # # Maintain heap property
        # while self.heap[next_vertex_index] is not None and self.heap[parent(next_vertex_index)] is not None \
        #         and self.heap[next_vertex_index] < self.heap[parent(next_vertex_index)]:
        #     self.swap(next_vertex_index, parent(next_vertex_index))
        #     next_vertex_index = parent(next_vertex_index)

    def extract_min(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.heapify(0)
        return minimum

    def show(self):
        print('heap', self.heap)
        print('positions', self.positions)


# Assume source is 1 (or in this case, 0 due to the zero based indexing convention)
def dijkstra(adjacency_list, vertices, src=0):
    # Get a count of all the vertices
    vertices_count = len(vertices)

    # Initialize heap
    h = Heap(vertices_count + 1)

    # Watch/Manage distances from source (for example, distances[5] = 8 means the distance from the source to 5 is 8)
    distances = []

    # Runs V times
    for vertex_index in range(vertices_count):
        distances.append(sys.maxint)
        h.insert([vertex_index, distances[vertex_index]])

    h.show()

    # While heap is not empty
    # while h.is_empty() is False:
    #     # u node in heap with smallest dist
    #     # remove u from heap
    #     u = h.extract_min()
    #     print(u)
    #
    #     # for each neighbor v of u according to adjacency list:
    #     # neighbor is in format [neighborVertex, distanceFromIndexVertex]
    #     for [neighborVertex, distanceFromIndexVertex] in adjacency_list[u]:
    #         print('neighbor of', u, 'is', neighborVertex, 'with distance', distanceFromIndexVertex)
    #         acc = dist[u] + distanceFromIndexVertex
    #         print('acc', acc)
    #         # If shorter distance was found (?)
    #         if acc < dist[neighborVertex]:
    #             dist[neighborVertex] = acc
    #             prev[neighborVertex] = u
    #             break

    print('done')

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
                # Use '-1' to transform edges into index-friendly integers
                edge_1 = int(split_line[0]) - 1
                edge_2 = int(split_line[1]) - 1
                weight = int(split_line[2])
                edges.append([edge_1, edge_2, weight])
                vertices.add(edge_1)
                vertices.add(edge_2)
        except EOFError:
            break

    if e != len(edges):
        print('You may be missing an edge or may have entered extra edges. Please check your input.')

    # Create graph representation - first element in list is the connected vertex, second element is the weight
    adjacency_list = [None] * n
    for edge in edges:
        if adjacency_list[edge[0]] is None:
            adjacency_list[edge[0]] = [[edge[1], edge[2]]]
        else:
            adjacency_list[edge[0]].append([edge[1], edge[2]])

    # Run Dijkstra's algorithm on the built graph
    dijkstra(adjacency_list, vertices)


if __name__ == '__main__':
    main()
