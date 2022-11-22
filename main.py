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


def lt_child(index):
    return (2 * index) + 1


def rt_child(index):
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

    # Set the position of the source vertex to its index in the positions array
    def setup(self, src):
        self.positions[src] = src

    def is_empty(self):
        return self.size == 0 or len(self.heap) == 0

    def leaf(self, index):
        return index > (self.size / 2) - 1

    def heapify(self, index):
        heapify_at_index = index
        left_child_index = lt_child(index)
        right_child_index = rt_child(index)

        if left_child_index < self.size - 1 and self.heap[left_child_index][1] < self.heap[heapify_at_index][1]:
            heapify_at_index = left_child_index

        if right_child_index < self.size - 1 and self.heap[right_child_index][1] < self.heap[heapify_at_index][1]:
            heapify_at_index = right_child_index

        if heapify_at_index != index:
            self.swap(heapify_at_index, index)
            self.heapify(heapify_at_index)

    def decrease_key(self, vertex, distance):
        # Update the distance value of the vertex in question
        pos_of_vertex_in_heap = self.positions[vertex]
        self.heap[pos_of_vertex_in_heap][1] = distance

        # While the distance value of the vertex is less than that of its parent
        while self.heap[pos_of_vertex_in_heap] is not None and self.heap[parent(pos_of_vertex_in_heap)] is not None \
                and self.heap[pos_of_vertex_in_heap][1] < self.heap[parent(pos_of_vertex_in_heap)][1]:
            # Bubble up the lower value to maintain min heap property
            self.swap(pos_of_vertex_in_heap, parent(pos_of_vertex_in_heap))
            # Check again
            pos_of_vertex_in_heap = parent(pos_of_vertex_in_heap)

    # Swap two vertices in the heap and positions watcher
    def swap(self, first_index, second_index):
        # Heap
        temp_heap_val = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp_heap_val

        # Positions watcher
        temp_pos_val = self.positions[first_index]
        self.positions[first_index] = self.positions[second_index]
        self.positions[second_index] = temp_pos_val

    def insert(self, vertex):
        if self.size >= self.max_size:
            return

        self.heap[self.size] = vertex
        self.positions[self.size] = vertex[0]
        self.size += 1

    def vertex_is_in_heap(self, vertex):
        return self.positions[vertex] < self.size

    # Returns the vertex with the lowest distance
    def extract_min(self):
        # Get the minimum
        minimum = self.heap[0]

        # Swap the new minimum with the last entry in the heap (aka the one with the largest distance value)
        self.swap(0, self.size - 1)

        # Decrease size
        self.size -= 1

        self.heapify(0)
        return minimum

    def show(self):
        print('heap', self.heap)
        print('positions', self.positions)
        print('size', self.size)


# Assume source is 1 according to assignment instructions (or in this case, 0 due to the zero-based indexing convention)
def dijkstra(adjacency_list, vertices, src=0):
    # Get a count of all the vertices
    vertices_count = len(vertices)

    # Initialize heap
    h = Heap(vertices_count + 1)

    # Watch/Manage distances from source (for example, distances[5] = 8 means the distance from the source to 5 is 8)
    distances = []
    previous = []

    # Runs V times
    for vertex_index in range(vertices_count):
        distances.append(sys.maxint)
        previous.append(sys.maxint)
        h.insert([vertex_index, distances[vertex_index]])

    h.setup(src)
    distances[src] = 0
    h.decrease_key(src, 0)

    # While heap is not empty
    while h.is_empty() is False:
        # u is the node in heap with the smallest distance
        # in the first iteration, it will be the source node
        u = h.extract_min()
        min_vertex = u[0]

        if adjacency_list[min_vertex] is None:
            continue

        # for each neighbor v of u according to adjacency list:
        # neighbor is in format [neighborVertex, distanceFromMinVertex]
        for incident_vertex in adjacency_list[min_vertex]:
            if distances[min_vertex] == sys.maxint:
                continue

            [neighbor_vertex, distance_from_min_vertex] = incident_vertex

            if h.vertex_is_in_heap(neighbor_vertex) is False:
                continue

            print('neighbor of', min_vertex, 'is', neighbor_vertex, 'with distance', distance_from_min_vertex)

            accumulated_distance = distances[min_vertex] + distance_from_min_vertex
            print('accumulated_distance', accumulated_distance)

            # If shorter distance was just discovered from source to the neighboring vertex
            if accumulated_distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = accumulated_distance
                h.decrease_key(neighbor_vertex, accumulated_distance)

    h.show()

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
