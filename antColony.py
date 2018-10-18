from igraph import *
import random
import copy
import random
def populacaoFormigas(grafo, quant):

	pop = []
	for i in range(0, quant):
		formiga = []
		formiga.append(random.randint(0, (grafo.vcount())-1)) ## definindo o vértice inicial, esse é o index dele
		formiga.append([])
		pop.append(formiga) ## primeira posição é onde ela começa


	return pop

def calculaIndexAresta(i, j):

	try:
		return grafo.get_eids(pairs = [ (i, j) ])
	except:
		return []

def fazCalculo(matriz, i, matrizProbabilidade):

	for j in range(0, (grafo.vcount())):

		k = calculaIndexAresta(i, j)
		#print(k)
		if len(k) != 0:
			eq1 = (matriz[i][j] ** alfa) * ((1/grafo.es['weight'][k[0]])**beta)
			eq2 = calculoGlobal(matriz, i)
			matrizProbabilidade[i][j] = eq1/eq2
		else:
			matrizProbabilidade[i][j] = 0

	#return matrizProbabilidade



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


def roleta(posicaoInicial, visitados, probabilidades): ### dada uma formiga eu tenho a posição inicial dele e os vértices que ele já visitou
### probabilidades é dada pelas probabilidades dos vértices
	somaTotal = 0
	for i in range(0, len(probabilidades)):
		if not i in visitados:
			somaTotal =  probabilidades[i] + somaTotal ### soma total da nossa roleta

	if somaTotal == 0:
		return -1

	proporcao = []
	for i in range(0, len(probabilidades)):

		if not i in visitados:
			proporcao.append(probabilidades[i]/somaTotal) ### proporção de cada um dos vértices
		else:
			proporcao.append(0)

	acumulador = 0
	escolhido = random.uniform(0, 1)
	for i in range(0, len(proporcao)):
		acumulador = proporcao[i] + acumulador
		if acumulador >= escolhido:
			return i ### i irá ser o vértice selecionado

def calculoFitness(caminho, grafo):

	soma = 0
	for i in range(1, len(caminho)):
		idVertice = grafo.get_eids(pairs = [ (caminho[i-1], caminho[i]) ])
		for j in idVertice:
			soma = grafo.es[j]['weight'] + soma
			break

	return soma

if __name__ == '__main__':
	
	random.seed()
	grafo = Graph.Read_GraphML("grafo.gml")
	matriz = list(grafo.get_adjacency(type = GET_ADJACENCY_BOTH, eids = False)) ## vai ser minha matriz de feromonios
	pop = populacaoFormigas(grafo, 10)
	numeroIteracoes = 100
	matrizProbabilidade = copy.copy(list(matriz))
	alfa = 0.7
	beta = 1-alfa
	melhores = []
	caminhosMelhores = []
	for i in range(0, numeroIteracoes):

		matrizProbabilidade = list(grafo.get_adjacency(type = GET_ADJACENCY_BOTH, eids = False))

		for j in range(0, grafo.vcount()):

			for k in range(0, len(matrizProbabilidade)):
				fazCalculo(matriz, k, matrizProbabilidade) ### calcula a matriz de probabilidades

			#### agora tenho que fazer a formiga decidir para onde ela irá
			for k in range(0, len(pop)):
				### uma formiga em um vértice i irá para um vértice j de acordo com a probabilidade da roleta
				novaP = roleta(pop[k][0], pop[k][1], matrizProbabilidade[pop[k][0]])
				if novaP == -1: break
				pop[k][1].append(pop[k][0]) ### adicionando o novo vértice como visitado
				pop[k][0] = novaP ## recebendo a nova posição da formiga

		fitness = []
		for k in range(0, len(pop)):

			fitness.append(calculoFitness(pop[k][1], grafo))

		melhores.append(max(fitness))
		caminhosMelhores.append(pop[fitness.index(max(fitness))][1])

	print(max(melhores))
	print(caminhosMelhores[melhores.index(max(melhores))])





		

