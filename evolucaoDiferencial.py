import random
import numpy as np
import math

def funcaoUm(n):
	y=0
	for i in n:
		y = i*i+y

	fx = -0.2*math.sqrt(1.0/2*y)

	return fx

def funcaoDois(n):

	y=0
	for i in n:
		y = math.cos(2*math.pi*i)+y

	fx = float(1.0/(len(n)))*y

	return fx

def funcaoFinal(n): ### definindo a função final
	fx = -20*math.exp(funcaoUm(n)) - math.exp(funcaoDois(n)) + 20 + math.exp(1)  
	return fx

def defineIndividuos():
	populacao = []
	for i in range(0, 100):
		aux = list(np.random.uniform(low =-.5, high=.5, size=(5,)))
		populacao.append(aux)

	return populacao

def mutacaoIntermediaria(populacao, fatorPertubacao):

	popIntermed = []
	for k in range(0, len(populacao)):

		selecionados = [] ### selecionando os individuos
		for j in range(0, 3): selecionados.append(random.randint(0, len(populacao)-1))

		individuoNovo = []
		for i in range(0, len(populacao[selecionados[0]])): ### que ai eu já to pegando do tamanho do individuo
			
			individuoNovo.append(populacao[selecionados[0]][i] + fatorPertubacao*(populacao[selecionados[1]][i]-populacao[selecionados[2]][i]))



		popIntermed.append(individuoNovo)


	return popIntermed


def cruzamento(filho, pai, coefCruzamento):

	novoFilho = []
	for i in range(0, len(filho)):
		
		x = random.uniform(0, 1)

		if x >= coefCruzamento: ### então eu recebo o gene do pai

			novoFilho.append(pai[i])
			
		else: ##recebo o gene do pai

			novoFilho.append(filho[i])


	return novoFilho


if __name__ == '__main__':
	
	fatorPertubacao = 1.2 ### fator de pertubação
	coefCruzamento = 0.8 ### coeficiente de cruzamento
	random.seed()
	numGeracoes = 100
	populacao = defineIndividuos() ### iniciei a populacao
	melhores = []
	flag = 0
	for i in range(0, numGeracoes):


		popIntermed = mutacaoIntermediaria(populacao, fatorPertubacao)
		filhos = []

		for k in range(0, len(populacao)):
			
			filhos.append(cruzamento(popIntermed[k], populacao[k], coefCruzamento))

		valorFitnessFilhos = list(map(funcaoFinal, filhos))
		valorFitnessPai = list(map(funcaoFinal, populacao))

		novaPop = []

		for k in range(0, len(valorFitnessFilhos)):
			if valorFitnessFilhos[k] < valorFitnessPai[k]:
				novaPop.append(filhos[k])
			else:
				novaPop.append(populacao[k])

		populacao = []
		populacao = novaPop

		if min(valorFitnessFilhos) < min(valorFitnessPai):
			melhores.append(min(valorFitnessFilhos))
		else:
			melhores.append(min(valorFitnessPai))
			
		populacao = novaPop
		flag = flag + 1

	print(melhores)



