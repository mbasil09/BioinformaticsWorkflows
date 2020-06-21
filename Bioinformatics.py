# Python program to print all paths from a source to destination. 
from collections import defaultdict 
from copy import deepcopy
import mysql.connector

#This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices 
		self.graph = defaultdict(list) 
		self.names = {}

	# function to add an edge to graph 
	def addEdge(self,u,v,name): 
		self.graph[u].append(v) 
		self.names[(u,v)] = name

	def printAllPathsUtil(self, u, d, visited, path, paths): 
		#DFS

		# Mark the current node as visited and store in path 
		visited[u]= True
		path.append(u) 

		# If current vertex is same as destination, then print 
		# current path[] 
		if u ==d:
			temppath = deepcopy(path)
			paths.append(temppath)
		else: 
			# If current vertex is not destination 
			#Recur for all the vertices adjacent to this vertex 
			for i in self.graph[u]: 
				if visited[i]==False: 
					self.printAllPathsUtil(i, d, visited, path, paths) 
					
		# Remove current vertex from path[] and mark it as unvisited 
		path.pop() 
		visited[u]= False


	# Prints all paths from 's' to 'd' 
	def printAllPaths(self,s, d): 
		paths=[]

		# Mark all the vertices as not visited 
		visited =[False]*(self.V) 

		# Create an array to store paths 
		path = [] 

		# Call the recursive helper function to print all paths 
		self.printAllPathsUtil(s, d,visited, path ,paths)
		return paths 




database = mysql.connector.connect(host="remotemysql.com",user="FkbucR2OLA",password="SdWDVN1cid",database="FkbucR2OLA")
cursor = database.cursor()

cursor.execute("select * from Nodes")
fetched_nodes = cursor.fetchall()

n = cursor.rowcount
graph = Graph(n+1) 

names = {}
for i in fetched_nodes:
	names[i[0]] = i[1]
nums = {v.lower(): k for k, v in names.items()}

cursor.execute("select * from NodeRelations")
fetched_relations = cursor.fetchall()
for i in fetched_relations:
	cmd = "select * from `Relations` where relationid="+str(i[2])
	cursor.execute(cmd)
	relation = cursor.fetchone()
	graph.addEdge(i[0],i[1],relation[1]) 




while(1):
	src = input("what type of data do you have? ")
	src = nums[src.lower()]
	term = input("what type of data do you need? ")
	term = nums[term.lower()]

	order = graph.printAllPaths(src,term)
	for j in range(len(order)):
		print("Method-"+str(j+1))
		for i in range(len(order[j])-1):
			print("step " + str(i+1) + ": " + names[order[j][i]] +" to "+names[order[j][i+1]] + " can be done using "+graph.names[(order[j][i]),order[j][i+1]])
		print()


