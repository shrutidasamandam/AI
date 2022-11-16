from graph import Graph
from queue import PriorityQueue

def uniform_cost_search(graph, start_node, goal_node):
  queue=PriorityQueue()
  queue.insert([start_node],0)
  while not queue.is_empty():
      node=queue.remove()
      current=node[1][len(node[1])-1]
      if goal_node in node[1]:
          print("Path found:" str(node[1]) ",Cost=" str(node[0]))
          break

      cost=node[0]
      for i in graph[current]:# This line is causing the error
        temp=node[1][:]
        temp.append(i)
        queue.insert(temp,cost graph[current][i])

if __name__ == "__main__":


 graph = Graph()

  # setting up nodes and neighbours
 graph.edges = {
    'A': set(['B', 'D']),
    'B': set(['C']),
    'C': set(['E', 'G']),
    'D': set(['E','F']),
    'E': set(['B']),
    'F': set(['G']),
    'G': set(['E'])
  }

 # setting up connection costs
 graph.weights = {
    'AB': 5, 'AD': 3,
    'BC': 1,
    'CE': 6, 'CG': 8,
    'DE': 2, 'DF': 2,
    'EB': 4,
    'FG': 3,
    'GE': 4
 }

uniform_cost_search(graph, 'A', 'C')
