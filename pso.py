import math
import funcao_pso
import random
import numpy as np
import matplotlib.pyplot as plt

def iniciaPopulacao(k):

	populacao = []

	for i in range(0, k):
		populacao.append(random.uniform(-1,2))

	return populacao


def conhecidos(quantConhecidos, k):

	conhecidosK = []
	for i in range(0, quantConhecidos):
		
		while(1):
			aux = random.randint(0, k-1)
			if not aux in conhecidosK:
				conhecidosK.append(aux)
				break

	return conhecidosK

def defineMelhorGlobal(vizinhos, fit):

	vizinhosFit = []
	for i in range(0, len(vizinhos)):
		vizinhosFit.append(fit[vizinhos[i]])

	return vizinhosFit.index(max(vizinhosFit))


def defineVelocidade(v, melhorGlobal, melhorIndividual, x):

	return coeficienteInercia * v + c1*r1*(melhorIndividual-x) + c2*r2*(melhorGlobal-x) 

def atualizaX(x, v):

	return x + v

def grafica(x1):

	x = np.array(range(len(x1)))

	#plt.plot( x, x1, 'go') # green bolinha
	plt.plot( x, x1,color='red') # linha pontilha orange

	#plt.plot( x, x2, 'r^') # red triangul

	#plt.axis([-10, 60, 0, 11])
	plt.title("Algoritmo PSO")


	plt.grid(True)
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()

if __name__ == '__main__':

	k = 10
	quantConhecidos = 3
	random.seed()
	populacao = iniciaPopulacao(k)
	velocidadeAtual = [0 for i in range(0, k)] ### definindo a velocidade do individuo
	coeficienteInercia = 0.5
	#### definindo constantes
	c1 = 1.2
	c2 = 1.5
	quantGeracoes = 100
	melhores = []
	for g in range(0, quantGeracoes):
		####### verificar critério
		fit = list(map(funcao_pso.funcaoObjetivo, populacao))
		###### define conhecidos
		vizinhos = []
		for i in range(0, k):
			vizinhos.append(conhecidos(quantConhecidos, k))
		###### sortear dois números aleatórios
		r1 = random.uniform(0, 1)
		r2 = random.uniform(0, 1)
		###### determinar a melhor posição individual e global
		melhorGlobal = fit.index(max(fit)) ### é o index do melhor de todos
		melhores.append(max(fit))
		melhorIndividual = []
		for i in range(0, k):
			melhorIndividual.append(defineMelhorGlobal(vizinhos[i], fit))  ### o global vai ser o melhor entre os vizinhos
		#### atualizar velocidade
		novaVelocidade = []
		for i in range(0, k):
			novaVelocidade.append(defineVelocidade(velocidadeAtual[i], melhorGlobal, melhorIndividual[i], populacao[i]))
		### atualizar posições
		novaPopulacao = list(map(atualizaX, populacao, velocidadeAtual))

		populacao = novaPopulacao
		velocidadeAtual = novaVelocidade

	grafica(melhores)



