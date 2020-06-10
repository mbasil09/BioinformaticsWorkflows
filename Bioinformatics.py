# Python program to print all paths from a source to destination. 

from collections import defaultdict 
from copy import deepcopy

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



# Create a graph given in the above diagram 

graph = Graph(18) 
names = {0:"GeoID", 1:"fastsanger", 2:"BAM", 3:"countMatrix", 4:"Differential Analysis", 5:"Gene Ontologies", 6:"Heatmap", 7:"SAM",
         8:"Drug name", 9:"drug ID", 10:"drug pathway", 11:"chemical compound name", 12:"compound features", 13:"DNA Sequence", 
         14:"RNA Sequence", 15:"Protein Sequence", 16:"Sequence", 17:"sequence features"}
# nums = {0:"Download SRR Accessions", 1:"FastQC", 2:"Alignemt", 3:"countMatrix",4:"Differential Analysis", 5:"Gene Ontologies", 6:"Heatmap"}
nums = {v.lower(): k for k, v in names.items()}

graph.addEdge(0, 1, "Download fastsanger files using SRR Accesions from NCBI using the GeoID") 
graph.addEdge(1, 2, "Bowtie2") 
graph.addEdge(2, 3, "featureCounts") 
graph.addEdge(3, 4, "DESeq2") 
graph.addEdge(4, 5, "geoseq") 
graph.addEdge(5, 6, "heatmap2") 
graph.addEdge(1, 7, "BWA")
graph.addEdge(7, 2, "Picard")
graph.addEdge(8, 9, "<name of some drug database to get drug ID>")
graph.addEdge(9, 10, "SMPDB")
graph.addEdge(11, 12, "FooDB")
graph.addEdge(16, 13, "check compostion of sequence to determine the biomolecule(ATGC for DNA)")
graph.addEdge(16, 14, "check compostion of sequence to determine the biomolecule(AUGC for RNA)")
graph.addEdge(16, 15, "check compostion of sequence to determine the biomolecule(Amino Acids for Protein)")
graph.addEdge(13, 17, "common DNA features are: ATGC composition, mass, length, etc")
graph.addEdge(14, 17, "common RNA features are: AUGC composition, mass, length, etc")
graph.addEdge(15, 17, "common Protein features are: Amino Acid composition, mass, length, charge etc")



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

