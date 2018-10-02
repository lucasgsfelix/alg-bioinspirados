import random
from igraph import *

alfa = 0.08
beta = 0.05
def definePop(numberOfIndividuals, graph):
	
	ants = []
	for i in range(0, numberOfIndividuals):
		ants.append(graph.vs[random.randint(0, graph.vcount()-1)]['id']) ### adicionei o id dos vértices
	
	return ants # in this method we will return the vertex of each ant

def fitness(k):
	somaDistancias = 0
	i=0
	while(i<len(individuo)-1):
		par = []
		for v in grafo.vs:
			if v['id'] == individuo[i]:
				par.append(v.index)
			if v['id'] == individuo[i+1]:
				par.append(v.index)
		
		if len(par)>1:idsArestas = grafo.get_eids(pairs = [(par[0], par[1])])

		pesos = []
		for k in range(0, len(idsArestas)):## assim eu pego o peso da arestas de id x grafo.es[idsArestas[0]]['weight']
			pesos.append(grafo.es[idsArestas[k]]['weight'])
		menorPeso = min(pesos)

		somaDistancias = menorPeso + somaDistancias ### somando o peso da menor distancia entre os vertices

		i=i+1

	return somaDistancias

def calculateJk(graph, kVisited): ## give the graph and k been k a vertex, this function will calculate the list of vertex not visited yet
	
	notVisited = []
	for i in graph.vs():
		if not i in kVisited: 
			notVisited.append(i)
	return notVisited

def defineAntsGenes(graph, pop):
	completePop = []
	index = 0
	for j in range(0, len(pop)):
		individual = []
		individual.append(j) ## id
		for k in range(0, len(graph.vs['id'])):
			if graph.vs['id'][k] == pop[j]: ## will get the index of the vertex
				index = k 
				break

		edgesId = []
		flag = 0 ## this flag will avoid the loop to go all the way
	
		for k in range(0, len(graph.get_edgelist())): ### will get the id of the edges
			

			if index in graph.get_edgelist()[k]:
				edgesId.append(k) ## k is the index of the edge
				flag = 1
				
		individual.append( [1] * graph.degree(index, mode = OUT, loops = True)) ### tij --> matrix of feromonios		
		individual.append(edgesId) ### id of all egdes
		individual.append([]) ### visited vertex
		completePop.append(individual)

	return completePop

def buildSolution(graph, k): ## this method will be responsible for build the solution calculating Pij
	

	### in the index = 1 theres is the genes
	tijGlobal = calculateTijGlobal(graph, 1)
	pij = []

	for i in range(0, len(k[1])):
		pij.append(((k[1][i] ** alfa) * ( graph.es['weight'][k[2][i]] ** beta ))/(tijGlobal))



def calculateTijGlobal(graph, tijGlobal):

	if tijGlobal == 1:
		soma = 0
		for i in range(0, graph.ecount()):
			soma = (tijGlobal**alfa)*(graph.es['weight'][i]**beta) + soma
	else:
		pass

	return soma

if __name__ == "__main__":
	
	random.seed()
	graph = Graph.Read_GraphML("grafo.gml") ## will read the graph file
	numberOfGenerations = 100
	pop = definePop(100, graph)
	pop = defineAntsGenes(graph, pop) 
	

	for k in range(0, numberOfGenerations):
		for ant in pop:
			buildSolution(graph, ant)