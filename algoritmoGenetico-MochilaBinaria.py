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
		somaRestricao = somaRestricao + (preco[i]*elementosX[i])

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

def definePopTotal(populacao):
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

	return popTotal

def selecionaMelhorElemento(popTotal, preco, capacidadeTotal):

	maiorElemento =  popTotal[0][2]
	p = 0
	for i in range(1, len(popTotal)):

		if maiorElemento <= popTotal[i][2]:
			if restricao(preco, popTotal[i][1], capacidadeTotal): ### o melhor elemento respeita a restrição
				maiorElemento = popTotal[i][2]
				p = i

	return maiorElemento, p

def selecaoRanking(popTotal):


	popTotal.sort(key=lambda x: x[2]) ### de acordo com fitness

	i=0 ### o último vai ser o melhor 
	childs = []
	while(i<len(popTotal)-2):
		childs.append(cruzamento(popTotal[i], popTotal[i+1]))
		i = i+2

	return childs

def cruzamento(individuo1, individuo2): #### e agora ?? como fazer o cruzamento ??
	
	child = []
	if len(individuo1[1]) % 2 == 0: ## tem um número de genes par, vai ser metade de um, metade de outro

		for i in range(0, int(len(individuo1[1])/2)):
			child.append(individuo1[1][i])

		for i in range(int(len(individuo2[1])/2), int(len(individuo2[1]))):
			child.append(individuo2[1][i])

	else: ### impar

		menor = (len(individuo1[1]-1)/2)
		maior = menor + 1
		if individuo1[2] >= individuo2[2]: ## então vai ter mais genes do pai com maior fitness

			for i in range(0, maior):
				child.append(individuo1[1][i])
			for i in range(maior, len(individuo2)):
				child.append(individuo2[1][i])

		else:

			for i in range(0, maior):
				child.append(individuo2[1][i])
			for i in range(maior, len(individuo1)):
				child.append(individuo1[1][i])
	return child


def mutacao(populacao, taxaMutacao):


	for i in range(0, len(populacao)):

		if random.uniform(0, 1) <= taxaMutacao:

			geneQueIraZerar = random.randint(0, len(populacao)-1)
			geneQueIraVirarUm = random.randint(0, len(populacao)-1)

			populacao[i][geneQueIraZerar] = 0
			populacao[i][geneQueIraVirarUm] = 1

	return populacao

if __name__ == '__main__':	
	
	random.seed()

	utilidade = [11, 21, 31, 33, 43, 53, 55, 65]
	preco = [1,11,21,23,33,43,45,55]	
	quantGeracoes = 100
	populacao = defineIndividuos(100, utilidade) ### definindo minha população inicial
	taxaMutacao = 0.01

	flagMelhorElemento = 0

	capacidadeTotal = 100

	cont = 0
	### começando o processo
	melhores = []
	for i in range(0, quantGeracoes):

		popTotal = definePopTotal(populacao)
		melhorElemento, p = selecionaMelhorElemento(popTotal, preco, capacidadeTotal)

		melhores.append(melhorElemento)
		################# verificando o melhor elemento
		if flagMelhorElemento == 0:
			ancientOne =  melhorElemento
			ancientP =  p
			flagMelhorElemento = 1
		else:

			if melhorElemento < ancientOne:
				cont=cont+1
				if cont == int(quantGeracoes/10):
					taxaMutacao = 0.05
					cont = 0
			else:
				### atualizando melhor melhor elemento
				ancientOne =  melhorElemento
				ancientP = p
				cont = 0

		#### seleção e cruzamento
		genesMelhor = populacao[p]
		populacao = selecaoRanking(popTotal) ### já fazendo seleção e cruzamento de uma vez
		populacao.append(genesMelhor)
		#### mutação
		populacao = mutacao(populacao, taxaMutacao)

	print(melhores)







		



		





