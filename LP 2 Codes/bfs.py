graph = {
    'A' :['B','C'],
    'C' :['F'],
    'H' :['D'],
    'E' :['F','H'],
    'F' :[],
    'B' :['H','E'],
    'D' :[],
}
visited =[]
queue =[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print (s,end="")
        for neighbour in graph [s]:
          if neighbour not in visited:
             visited.append(neighbour)
             queue.append(neighbour)
 #driver code
bfs(visited, graph, 'A')
