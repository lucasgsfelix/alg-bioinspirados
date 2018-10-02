import random
from igraph import *
def definePop(numberOfIndividuals, graph):
	
	ants = []
	for i in range(0, numberOfIndividuals):
		ants.append(random.randint(0, graph.vcount()-1))
	
	return ants # in this method we will return the vertex of each ant

def buildSolution(graph, k): ## this method will be responsible for build the solution calculating Pij
	

	


def fitness(k):
	pass

def calculateJk(graph, kVisited): ## give the graph and k been k a vertex, this function will calculate the list of vertex not visited yet
	
	notVisited = []
	for i in graph.vs():
		if not i in kVisited: 
			notVisited.append(i)
	return notVisited
	

if __name__ == "__main__":
	
	random.seed()
	graph = Read_GraphML("grafo.gml") ## will read the graph file
	numberOfGenerations = 100
	pop = definePop(100, graph)
	
	completePop = []
	for j in range(0, len(pop)):
		individual = []
		individual.append(for i in range(0, graph.degree(pop[j], mode = ALL, loops = True))) ### tij --> matrix of feromonios		
		individual.append() ### number of visited vertices
		completePop.append(individual)

	for k in range(0, numberOfGenerations):
		
		
		
		
			
