### desenvolvido por lucas félix

import random


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


def restricao(capacidade, mochila, peso, utilidade):


	soma = 0
	for i in range(0, len(utilidade)):

		if utilidade[i] in mochila:
		
			soma = soma + peso[i]
	


	if soma > capacidade:
		return False
	else:
		return True ### vai ser verdade se ele respeita a restrição



def funcFit(mochila, utilidade):

	fit = 0

	for i in utilidade:


		if i in (mochila):

			fit = fit + i


	return fit

def retiraRepetidos(childOne):
	i=0
	while(i<len(childOne)):
		aux = childOne[i]
		j=0
		cont = 0
		while(j<len(childOne)):
			if aux == childOne[j]:
				cont = cont + 1
			if cont>1:
				childOne.pop(j)
				j=j-1
			j=j+1
		i=i+1
	return childOne

		


def cruzamento(individuoOne, individuoTwo):

	childOne = []
	childTwo = []

	#### dividindo os individuos
	indOne_1 = individuoOne[0:int((len(individuoOne)/2))]
	indOne_2 = individuoOne[int((len(individuoOne)/2)):len(individuoOne)]

	indTwo_1 = individuoTwo[0: int(len(individuoTwo)/2)]
	indTwo_2 = individuoTwo[int(len(individuoTwo)/2):len(individuoTwo)]

	for i in indOne_1: childOne.append(i)
	for i in indTwo_2: childOne.append(i)
	for i in indTwo_1: childTwo.append(i)
	for i in indOne_2: childTwo.append(i)

	childOne = retiraRepetidos(childOne)
	childTwo = retiraRepetidos(childTwo)
	
	

	return childOne, childTwo

def mutacao(taxaMutacao, populacao, utilidade):

	for i in range(0, len(populacao)):
		aux = random.uniform(0, 1)
		if aux<= taxaMutacao:

			aux = random.randint(0, len(utilidade)-1) ###decidindo quem vai mudar

			if not utilidade[aux] in populacao[i]:
				populacao.append(utilidade[aux])
			else:
				k=0
				while(k<len(populacao[i])):

					if populacao[i][k] == utilidade[aux]:

						populacao[i].pop(k)
						break
					k=k+1

	return populacao



if __name__ == '__main__':
	
	random.seed()
	utilidade = [11, 21, 31, 33, 43, 53, 55, 65]
	peso = [1, 11, 21, 23, 33, 43, 45, 55]
	capacidade = 100


	quantGeracoes = 100
	populacao = geraPopulacao(100, utilidade)
	taxaMutacao = 0.01

	melhores = []
	melhorAntigo = 0
	cont = 0
	contMutacao = 0
	for i in range(0, quantGeracoes):


		popFit = []

		for i in range(0, len(populacao)):
			aux = []
			aux.append(i)
			aux.append(populacao[i])
			aux.append(funcFit(populacao[i], utilidade))
			popFit.append(aux)



		### seleciono o melhor elemento e penalizo os que não estão respeitando a restrição
		popFit.sort(key = lambda x: x[2], reverse =  True)
		### penalizando de acordo com a restrição

		flag = 0
		for i in range(0, len(popFit)):

			if restricao(capacidade, popFit[i][1], peso, utilidade): ### se respeita a restrição então é o meu melhor

				if flag==0:
					melhorValor = popFit[i][2] ## este melhor valor é de capacidade
					posicaoMelhor = i
					flag = 1

			else: ### não respeita minha restrição, então tenho que penalizar
				soma = 0
				for k in range(0, len(utilidade)):

					if utilidade[k] in popFit[i][1]:
					
						soma = soma  + peso[k]
				dif = soma-capacidade ### esse valor vai ser maior que minha capacidade
				porcentagem = (dif)/soma

				popFit[i][2] = popFit[i][2] - popFit[i][2]*(porcentagem) ### penalizando o fit

		

		if melhorAntigo == 0:
			melhorAntigo = melhorValor
			melhorP = posicaoMelhor

		else:

			if melhorValor>melhorAntigo:  ### eu tenho que atualizar esse valor

				melhorAntigo = melhorValor
				melhorP =posicaoMelhor
				cont = 0

			else: ### se for menor igual, então eu estou mantendo o melhor anterior
				### evitando mínimos locais
				melhorValor = melhorAntigo
				posicaoMelhor = melhorP
				cont= cont+1
				if cont == int(quantGeracoes/10): ## 10% das gerações
					contMutacao = contMutacao + 1
					taxaMutacao = 0.05 * contMutacao

		melhores.append(melhorValor) ### guardando os melhores valores de fit


		popFit.sort(key = lambda x: x[2], reverse = True) ## ordenando de acordo com o fit, fará a seleção por ranking
		
		k = 1
		populacaoNova = []
		while(k<len(popFit)):
			#### fazer o cruzamento
			childOne, childTwo = cruzamento(popFit[k-1][1], popFit[k][1])
			k=k+2 ### faço o cruzamento dos pais, que irá gerar dois filhos
			### o último casal só tem um filho
			if k !=  len(popFit)-1:
				populacaoNova.append(childTwo)
			populacaoNova.append(childOne)
		
		populacaoNova.append(populacao[melhorP]) ### colocando o melhor individuo na minha nova Populacao
		populacao = []
		populacao = populacaoNova ## atualizando a populacao

		populacao = mutacao(taxaMutacao, populacao, utilidade)

		k = 0
		while(k<len(populacao)):

			if type(populacao[k]) != list:

				populacao.pop(k)

				k=k-1

			k=k+1


	print(melhores)



