from igraph import *
import random
import copy
def populacaoFormigas(grafo, quant):

	pop = []
	for i in range(0, quant):
		formiga = []
		formiga.append(random.randint(0, (grafo.vcount())-1)) ## definindo o vértice inicial, esse é o index dele
		pop.append(formiga)

	return pop

def calculaIndexAresta(i, j):


	try:
		return grafo.get_eids(pairs = [ (i, j) ])
	except:
		return []

def fazCalculo(formiga, matriz, i, matrizProbabilidade):

	for j in range(0, (grafo.vcount())):

		k = calculaIndexAresta(i, j)
		#print(k)
		if len(k) != 0:
			eq1 = (matriz[i][j] ** alfa) * ((1/grafo.es['weight'][k[0]])**beta)
			eq2 = calculoGlobal(matriz, i)
			matrizProbabilidade[i][j] = eq1/eq2
		else:
			matrizProbabilidade[i][j] = 0


	return matrizProbabilidade



def calculoGlobal(matriz, i):

	soma = 0
	for j in range(0, len(matriz[i])):

		k = calculaIndexAresta(i, j)
		if len(k) != 0:
			soma = (matriz[i][j] ** alfa)*((1/grafo.es['weight'][k[0]]**beta)) + soma
		else:
			soma = soma + 0

	return soma

def funcaoObjetivo(grafo, individuo):

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


if __name__ == '__main__':
	
	grafo = Graph.Read_GraphML("grafo.gml")
	matriz = list(grafo.get_adjacency(type = GET_ADJACENCY_BOTH, eids = False)) ## vai ser minha matriz de feromonios
	pop = populacaoFormigas(grafo, 10)
	numeroIteracoes = 100
	matrizProbabilidade = copy.copy(list(matriz))
	alfa = 0.7
	beta = 1-alfa

	for i in range(0, numeroIteracoes):

		for k in range(0, len(pop)):

			fazCalculo(pop[k], matriz, k, matrizProbabilidade)
			### qual a fórmula para atualização da matriz de feromonios
			## agora eu tenho que decidir para onde eu vou

		

