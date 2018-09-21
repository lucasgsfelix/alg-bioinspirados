### desenvolvido por lucas félix
import random
import numpy as np
import matplotlib.pyplot as plt
def geraPopulacao(quantIndividuos, utilidade):

	populacao = []
	for i in range(0, quantIndividuos):

		tamanhoIndividuo = random.randint(1, len(utilidade)-1) ### de um ao tamanho do vetor de utilidade
		#### aqui estou definindo o tamanho do individuo

		j=0
		individuo = []
		while(j<(tamanhoIndividuo)):

			x = random.randint(0, len(utilidade)-1)
			if not utilidade[x] in individuo:
				individuo.append(utilidade[x])
				j=j+1

		populacao.append(individuo)

	return populacao

def funcFit(mochila, utilidade):

	fit = 0

	for i in utilidade:


		if i in (mochila):

			fit = fit + i


	return fit

def mutacaoIntermediaria(populacao, fatorPertubacao, utilidade): # baseado no método utilizado no trabalho DeCode
	
	popIntermed = []
	for k in range(0, len(populacao)):

		selecionados = [] ### selecionando os individuos
		for j in range(0, 3): selecionados.append(random.randint(0, len(populacao)-1))

		individuoNovo = listaDiferencial(populacao, selecionados)

		popIntermed.append(individuoNovo)


	return popIntermed

def listaDiferencial(populacao, selecionados):

	#primeiramente eu preciso das posições onde eles são diferentes (x2 e x3)

	# recebendo os genes
	x1 = populacao[(selecionados[0])]
	x2 = populacao[(selecionados[1])]
	x3 = populacao[(selecionados[2])]

	###como tem tamanhos diferentes
	naoPresentes = []
	for i in x3:
		if not i in x2:
			naoPresentes.append(i)
	genesMutados = int(fatorPertubacao*len(naoPresentes)) ## calculando a quantidade de genes que serão mutados

	for i in range(0, genesMutados):

		p = random.randint(0, len(x1)-1) ## selecionando a posição que será mutada
		item = random.randint(0, len(utilidade)-1)
		x1[p] = utilidade[item]


	return x1

def cruzamento(filho, pai, coefCruzamento):

	novoFilho = []
	for i in range(0, len(filho)):
		
		x = random.uniform(0, 1)

		if x >= coefCruzamento: ### então eu recebo o gene do pai

			try:
				novoFilho.append(pai[i])
			except:
				pass
			
		else: ##recebo o gene do pai
			try:
				novoFilho.append(filho[i])
			except:
				pass


	return novoFilho


def restricao(capacidade, mochila, peso, utilidade):


	soma = 0
	for i in range(0, len(utilidade)):

		if utilidade[i] in mochila:
		
			soma = soma + peso[i]
	


	if soma > capacidade:
		return False
	else:
		return True ### vai ser verdade se ele respeita a restrição



def verificaPune(fit, populacao, capacidade, peso, utilidade):
	

	if not restricao(capacidade, populacao, peso, utilidade): ## se não respeita minha restrição eu tenho que punir

		soma = 0
		for k in range(0, len(utilidade)):

			if utilidade[k] in populacao:
				soma = soma  + peso[k]

		dif = soma-capacidade ### esse valor vai ser maior que minha capacidade
		porcentagem = (dif)/soma

		fit = fit - fit*(porcentagem) ### penalizando o fit

	return fit

def imprimeGrafico(melhores):

	x = np.array(range(len(melhores))) ## fazendo o eixo x
	plt.plot(x, melhores)
	plt.title("ED para o problema da mochila")
	plt.grid(True) ### imprimindo as grades atrás
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()


if __name__ == '__main__':
	
	random.seed()
	utilidade = [11, 21, 31, 33, 43, 53, 55, 65]
	peso = [1, 11, 21, 23, 33, 43, 45, 55]
	capacidade = 100
	fatorPertubacao = 0.7
	coefCruzamento = 0.8
	quantGeracoes = 100
	populacao = geraPopulacao(100, utilidade)

	melhores = []
	idMelhores = []
	for k in range(0, quantGeracoes):

		popInterMed = mutacaoIntermediaria(populacao, fatorPertubacao, utilidade)

		filhos = []

		for i in range(0, len(popInterMed)):

			filhos.append(cruzamento(popInterMed[i], populacao[i], coefCruzamento))


		fitFilho = []
		fitPai = []

		for i in range(0, len(filhos)):

			fitFilho.append(funcFit(filhos[i], utilidade))
			fitPai.append(funcFit(populacao[i], utilidade))

		for i in range(0, len(fitFilho)): ## aqui eu verifico se respeita ou não minha restrição, caso não, há uma punição

			fitFilho[i] = verificaPune(fitFilho[i], filhos[i], capacidade, peso, utilidade)
			fitPai[i] = verificaPune(fitPai[i], populacao[i], capacidade, peso, utilidade)

		novaPop = []

		for i in range(0, len(fitFilho)):

			if fitFilho[i] >= fitPai[i]:
				novaPop.append(filhos[i])
			else:
				novaPop.append(populacao[i])

		populacao = novaPop

		if max(fitFilho)>max(fitPai):
			melhores.append(max(fitFilho))
			idMelhores.append(filhos[fitFilho.index(max(fitFilho))]) ## retorna o index do melhor valor
		else:
			melhores.append(max(fitPai))
			idMelhores.append(populacao[fitPai.index(max(fitPai))])


	print("O melhor fit é: ", max(melhores))
	print("Os itens do melhor são: ", idMelhores[melhores.index(max(melhores))])
	imprimeGrafico(melhores)











		




