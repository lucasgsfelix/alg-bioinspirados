### aula 23/08
import random

def fitness(utilidade, populacao):

	soma = 0
	for i in range(0, len(utilidade)):
		
		if populacao[i] == 1:
			soma = (utilidade[i]*1)+soma


	return soma

def restricao(preco, elementosX, capacidadeTotal):

	somaRestricao = 0
	for i in range(0, len(preco)):
		somaRestricao = somaRestricao + (preco[i]*elementosX)

	if somaRestricao<=capacidadeTotal: ### tenho valores válidos
		return True
	else:
		return False

def defineIndividuos(quantIndividuos, utilidade):
	
	populacao = []
	for i in range(0, quantIndividuos):
		individuo = []
		for j in range(0, len(utilidade)):
			aux = random.randint(0, 1)
			individuo.append(aux)

		populacao.append(individuo) ## adicionando o individuo na populacao

	return populacao

if __name__ == '__main__':
	
	random.seed()

	utilidade = [11, 21, 31, 33, 43, 53, 55, 65]
	elementosX = [0, 0, 0, 0, 0, 0, 0, 0]
	
	quantGeracoes = 100
	populacao = defineIndividuos(100, utilidade) ### definindo minha população inicial

	taxaMutacao = 0.01

	popFit = []
	popTotal = []
	##### definindo minha população
	for i in range(0, len(populacao)):
		popFit = []
		fit = fitness(utilidade, populacao[i]) ### calculando o fitness
		popFit.append(i) ### id da população
		popFit.append(populacao[i]) ### os genes do individuo
		popFit.append(fit) ### fitness daquele individuo
		popTotal.append(popFit)


	### começando o processo

	for i in range(0, quantGeracoes):

		





