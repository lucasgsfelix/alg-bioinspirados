#### aula 09/08 - algoritmo genetico

import math
import random
import numpy as np
#import matplotlib.pyplot as plt
import sys


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

def torneio(populacaoFitness):

	contesterOne = random.randint(0, len(populacaoFitness)-1)
	contesterTwo = random.randint(0, len(populacaoFitness)-1)
	
	if populacaoFitness[contesterOne][1]<=populacaoFitness[contesterTwo][1]:

		return populacaoFitness[contesterOne]

	else:

		return populacaoFitness[contesterTwo]

def cruzamentoBlend(individuo1, individuo2):

	alfa = 0.8
	dp = []
	aux = 0
	for i in range(0, len(individuo1)):

		aux = individuo1[i] - individuo2[i]
		if aux<0: aux * -1

		dp.append(aux)

	child = []
	for i in range(0, len(individuo1)):
		valor = random.uniform(min(individuo1[i],individuo2[i])-alfa*dp[i], max((individuo1[i],individuo2[i]))+alfa*dp[i])
		child.append(valor)


	return child


def cruzamento(bestOnes, bestOthers, populacao, flagFuncao):


	childs = []

	j = 0
	while(j<len(bestOnes)):

		p1 = bestOnes[j][0]
		p2 = bestOthers[j][0]


		if flagFuncao == 0: ### cruzamento mediano

			childs.append(cruzamentoMedio(populacao[p1], populacao[p2]))

		else: ## cruzamento blend alfa

			childs.append(cruzamentoBlend(populacao[p1], populacao[p2]))

		j=j+1

	return childs


def cruzamentoMedio(individuo1, individuo2):

	child = []
	for i in range(0, len(individuo1)):
		child.append(float((individuo1[i]+individuo2[i])/2))

	return child


def selecionaMelhorElemento(populacaoFitness):

	melhor = populacaoFitness[0][1]
	p = 0

	for i in range(0, len(populacaoFitness)):

		if populacaoFitness[i][1] < melhor:

			melhor = populacaoFitness[i][1]
			p = i


	return p, melhor


def selecaoPorRoleta(populacaoFitness):

	porcaoSelecionada = random.uniform(0, 1)
	porcaoSelecionada = 1/porcaoSelecionada
	acumulador = 0
	p = 0
	flag = 0
	for i in range(0, len(populacaoFitness)):
		acumulador = (1/populacaoFitness[i][1]) + acumulador
		if acumulador > porcaoSelecionada:
			p = i
			melhor = populacaoFitness[i][1]
			flag = 1
			break

	return populacaoFitness[p]


def imprimeSaida(melhores, flagFuncao):

	if flagFuncao == 0:
		arq = open("mediano.txt", 'w')
	else:
		arq = open("bledAlfa.txt", 'w')

		
	for i  in melhores:	
		arq.write(str(i)+'\n')
	arq.close()

def mutacao(populacao, taxaMutacao):

	for i in range(0, len(populacao)):

		for j in range(0, len(populacao[i])):
			
			
			x = random.uniform(0, 1)

			if x <= taxaMutacao: ### vou fazer a mutação

				novoGene = random.uniform(-5, 5)
				populacao[i][j] = novoGene

	return populacao

def imprimeGrafico(melhores, flagFuncao):

	x = np.array(range(len(melhores))) ## fazendo o eixo x
	plt.plot(x, melhores)
	if flagFuncao == 0:
		plt.title(" AG utilizando cruzamento Mediano ")
	else:
		plt.title("AG utilizando cruzamento BlendAlfa")
	plt.grid(True) ### imprimindo as grades atrás
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()



if __name__ == '__main__':
	
	populacao = defineIndividuos()
	taxaMutacao = 0.01 #### é bom entre 1% e 15%
	#### definindo os fitness da população
	quantidadeGeracoes = 100
	geracoesMelhores = 0
	flagMelhor =  0
	random.seed()
	melhores = []
	#flagFuncao = 0

	### passando a função que quero usar por parametro
	if len(sys.argv)>2:
		flagFuncao = sys.argv[1]
		nomeArqSaida = sys.argv[2]
		flagFuncao = int(flagFuncao)
	else:
		flagFuncao =  1


	for k in range(0, (quantidadeGeracoes)):


		valorFitness = []
		valorFitness = list(map(funcaoFinal, populacao))

		populacaoFitness = []
		

		for i in range(0, len(valorFitness)):
			aux = []
			aux.append(i) ### id 
			aux.append(valorFitness[i]) #valorFitness
			populacaoFitness.append(aux)
		

		p, melhorValor = selecionaMelhorElemento(populacaoFitness)
		melhorElemento = populacao[p]

		if flagMelhor == 0:
			melhorElemento = populacao[p]
			melhorAntigo = melhorValor
			flagMelhor = 1
		else:
			#print(k , "f(x) ", melhorAntigo, " x ", melhorValor)
			if melhorValor<melhorAntigo:
				geracoesMelhores = 0
				melhorElemento = populacao[p]
				melhorAntigo = melhorValor
			else:
				melhorValor = melhorAntigo ### atualizando o valor
				geracoesMelhores = geracoesMelhores + 1
				if(geracoesMelhores==int(quantidadeGeracoes/10)):
					taxaMutacao = 0.05 ### aumentando minha taxa de mutação caso eu haja uma convergência muito rápida
		melhores.append(melhorValor) ## meu x


		bestOnes = []

		selectionFlag = 0
		for i in range(0, len(populacaoFitness)-1): #### escolhendo os melhores por torneio

			if selectionFlag == 0:
				bestOnes.append(selecaoPorRoleta(populacaoFitness))
			else:
				bestOnes.append(torneio(populacaoFitness))

		bestOthers = []

		for i in range(0, len(populacaoFitness)-1): ### escolhendo os melhores por torneio

			if selectionFlag == 0:
				bestOthers.append(selecaoPorRoleta(populacaoFitness))
			else:
				bestOthers.append(torneio(populacaoFitness))

		populacao = cruzamento(bestOnes, bestOthers, populacao, flagFuncao)
		populacao.append(melhorElemento) ### adicionando o novo elemento de nossa população
		
		############# é hora de mutar
		populacao = mutacao(populacao, taxaMutacao)
	

	print("O melhor valor foi: ", melhorValor)

	if len(sys.argv) > 2:
		arq = open(nomeArqSaida, 'a')
		arq.write(str(min(melhores))+'\n')
		arq.close()
	#imprimeSaida(melhores, flagFuncao) # imprime saída no arquivo
	#imprimeGrafico(melhores) ### imprimindo os melhores
	
