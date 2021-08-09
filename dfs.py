class DFS:
    def dfs_creation(self, visited, graphs, node):
        graph = graphs
        if node not in visited:
            print (node)
            visited.append(node)
            for neighbour in graph[node]:
                self.dfs_creation(visited, graph, neighbour)

if __name__ == "__main__":
    user_graph = {
            'A' : ['B','C'],
            'B' : ['E'],
            'C' : ['F'],
            'D' : [],
            'E' : ["K"],
            'F' : ["D","H"],
            "K" : [],   
            "H" : []
        }

    visited = []
    # user = input("Your root: ")
    user = 'a'
    user = user.upper()
    obj = DFS()
    obj.dfs_creation( visited, user_graph, user)


    '''
            A
          /   \
         B     C
        /     /
       E     F
      /     / \
     K     D   H
    
    '''