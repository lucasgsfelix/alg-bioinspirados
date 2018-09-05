from igraph import *
import random

def definePopulacao(vertices):

	populacao = []

	for i in range(0, 100):

		individuo = []
		while(len(individuo)!=len(vertices)): ### vou ter todos os vértices em diferentes ordens
			
			x = random.randint(0, len(vertices)-1)
			if not vertices[x] in individuo:
				individuo.append(vertices[x])

		populacao.append(individuo)

	return populacao

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

def selecaoTorneio(popFit):

	selecionados = []
	for i in range(0, len(popFit)):

		lum = random.randint(0, len(popFit)-1)
		ldois =  random.randint(0, len(popFit)-1)

		if popFit[lum][2] < popFit[ldois][2]:

			selecionados.append(popFit[lum])

		else:

			selecionados.append(popFit[ldois])



	return selecionados

def cruzamentoCorte(paiUm, paiDois):


	pInicial = int(len(paiUm)/3)
	meioUm = paiUm[pInicial:pInicial*2] ### coloquei metade um  meio do filho 1
	meioDois = paiDois[pInicial:pInicial*2]

	filhoUm = []
	filhoDois = []
	for i in meioUm: filhoUm.append(i)
	for i in meioDois: filhoDois.append(i)

	for i in paiDois:
		if not i in filhoUm:
			filhoUm.append(i)
	for i in paiUm:
		if not i in filhoDois:
			filhoDois.append(i)

	return filhoUm, filhoDois

def mutacao(taxaMutacao, populacao):

	x = random.uniform(0, 1)

	if x <= taxaMutacao:

		p1 = random.randint(0, len(populacao)-1)
		p2 = random.randint(0, len(populacao)-1)


		x = populacao[p1]
		y = populacao[p2]

		populacao[p1] = y
		populacao[p2] = x

	return populacao


if __name__ == '__main__':
	
	random.seed()
	grafo = Graph.Read_GraphML("dj38.gml") ### lendo o grafo no formato gml
	populacao = definePopulacao(grafo.vs['id']) ### defini minha população inicial
	quantGeracoes = 100 #### definindo a quantidade de gerações
	antigoMelhor = 0
	cont = 0
	taxaMutacao = 0.01
	melhores = []
	for i in range(0, quantGeracoes):

		#### agora eu tenho que calcular o fitness da minha população
		popFit = []
		for k in populacao: ### adicionando tudo que preciso para fazer os calculos
			aux =[]
			aux.append(k.index)
			aux.append(k)
			fit = funcaoObjetivo(grafo, k)
			aux.append(fit)
			popFit.append(aux)


		popFit.sort(key = lambda x : x[2]) ## o menor é o melhor, pq é um problema de minimização
		melhorElemento = popFit[0]
		### meu melhor elemento sempre estará na posição zero
		melhores.append(melhorElemento[2])
		if antigoMelhor == 0:
			antigoMelhor = melhorElemento
		else:
			if antigoMelhor[2] > melhorElemento[2]:
				cont = cont + 1
				if cont == int(quantGeracoes/10):
					taxaMutacao = 0.05
			else: ### o que quer dizer que temos um novo melhor elemento
				antigoMelhor = melhorElemento

		selecionados = selecaoTorneio(popFit)
		### cruzamento

		k=0
		populacao = []
		while(k<len(selecionados)):
			filhoUm, filhoDois = cruzamentoCorte(selecionados[k][1], selecionados[k+1][1])
			populacao.append(filhoUm)
			populacao.append(filhoDois)
			k=k+2
		
		populacao.pop(len(populacao)-1) ### retirando o último elemento
		populacao.append(melhorElemento[1]) ### adicionando o melhor elemento da rodada anterior

		#### mutação

		for i in range(0, len(populacao)):

			populacao[i] = mutacao(taxaMutacao, populacao[i])



	print(melhores)














	
