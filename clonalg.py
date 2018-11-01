import random
import math
import numpy as np
import matplotlib.pyplot as plt
def geraPopulacao(numeroAntiCorpos, numeroIndividuos):

	populacao = []
	for i in range(0, numeroIndividuos):
		individuo = []
		for j in range(0, numeroAntiCorpos):
			individuo.append(random.uniform(-5, 5))
		populacao.append(individuo)


	return populacao

def calculoFitness(x):

	soma = 0
	for i in x:
		soma = i**2 + soma

	return soma

def selecionaClona(novaPop, quantSelecionados):


	selecionados = []
	cont = 0
	for i in range(0, quantSelecionados):
		selecionados.append(novaPop[i]) ### vão ser os anticorpos que definem os individuos
		cont = cont + 1

	quantidadeCopias=[]

	for i in range(0, len(selecionados)):
		quantidadeCopias.append(int(quantSelecionados-1/((1/novaPop[i][1])))) ## quantidade de copias

	populacao = []
	for i in range(0, len(quantidadeCopias)):
		for j in range(0, quantidadeCopias[i]):
			populacao.append(novaPop[i][0])

	populacao = mutacaoClones(taxaMutacao, populacao) ### passo 4 do algoritmo

	for i in range(0, len(novaPop)):
		populacao.append(novaPop[i][0])
	
	fitness = list(map(calculoFitness, populacao))
	novaPop = []
	for i in range(0, len(populacao)):
		individuo = []
		individuo.append(populacao[i])
		individuo.append(fitness[i])
		novaPop.append(individuo)

	novaPop.sort(key = lambda x : x[1])
	populacao = []
	for i in range(0, tamanhoPop-1):
		populacao.append(novaPop[i][0])

	return populacao



def mutacaoClones(taxaMutacao, populacao):
	
	for i in range(0, len(populacao)):

		aux = random.uniform(0, 1)

		if aux<=taxaMutacao:
			for k in range(0, len(populacao[i])):
				populacao[i][k] = random.uniform(-5 + min(populacao[i]), 5-max(populacao[i]))
				#populacao[i][k] = random.uniform(-5, 5)


	return populacao

def grafica(x1):

	x = np.array(range(len(x1)))

	#plt.plot( x, x1, 'go') # green bolinha
	plt.plot( x, x1,color='red') # linha pontilha orange

	#plt.plot( x, x2, 'r^') # red triangul

	#plt.axis([-10, 60, 0, 11])
	plt.title("Algoritmo ClonAlg")


	plt.grid(True)
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()

if __name__ == '__main__':
	
	random.seed()
	tamanhoPop =  100
	numGeracoes = 100 ### numero total de gerações
	populacao = geraPopulacao(3, tamanhoPop) ## gera população
	taxaMutacao = 0.1
	melhores = []
	genesMelhor = 0
	for i in range(0, numGeracoes):


		if i % 5 == 0 :
			populacao = mutacaoClones(taxaMutacao, populacao)
		if i > 0:
			populacao.append(genesMelhor)
		novaPop = []
		fitness = list(map(calculoFitness, populacao)) ### calculei o fitness
		for k in range(0, len(populacao)):
			individuo = []
			individuo.append(populacao[k])
			individuo.append(fitness[k])
			novaPop.append(individuo)

		
		novaPop.sort(key = lambda x : x[1])
		
		if i== 0:
			melhor = novaPop[0][1]
			genesMelhor = novaPop[0][0]
			melhores.append(melhor)
		else:
			if novaPop[0][1] < melhor:
				melhor = novaPop[0][1]
				genesMelhor = novaPop[0][0]
				melhores.append(melhor)
			else:
				melhores.append(melhor)
		quantSelecionados = int(tamanhoPop/10) ### quantidade de individuos que serão selecionados para ser clonada
		populacao = selecionaClona(novaPop, quantSelecionados)


	grafica(melhores)

		






