class GFG: 
	def __init__(self,graph): 
		self.graph = graph 
		self.left = len(graph) 
		self.right = len(graph[0]) 

	def bpm(self, u, matchR, seen): 
		for v in range(self.right): 
			if self.graph[u][v] and seen[v] == False: 
				seen[v] = True
                
				if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen): 
					matchR[v] = u 
					return True

		return False

	def maxBPM(self): 
		matchR = [-1] * self.right 
		
		result = 0
		for i in range(self.left): 
			seen = [False] * self.right 
			
			if self.bpm(i, matchR, seen): 
				result += 1

		return result 

def main():
    V, E = [int(x) for x in input().split()]
    bpGraph = [[int(0) for x in range(V)] for y in range(V)]

    for _ in range(E):
        x, y = [int(index) for index in input().split()]
        x -= 1
        y -= 1
        bpGraph[x][y] = 1
        bpGraph[y][x] = 1

    g = GFG(bpGraph) 

    print (int(g.maxBPM() / 2)) 


main()