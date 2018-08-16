import matplotlib.pyplot as plt
import numpy as np

def leitura(arquivo):

	arq = open(arquivo, 'r')
	info = arq.read()
	arq.close()
	info = info.split('\n')

	if (info[len(info)-1]==''):
		info.pop(len(info)-1)
	for i in range(0, len(info)):
		info[i] = float(info[i])

	return info

def grafica(x1, x2):

	x = np.array(range(len(x1)))

	#plt.plot( x, x1, 'go') # green bolinha
	plt.plot( x, x1,color='red') # linha pontilha orange

	#plt.plot( x, x2, 'r^') # red triangulo
	plt.plot( x, x2, color='green')  # linha tracejada azul

	#plt.axis([-10, 60, 0, 11])
	plt.title("Algoritmos genéticos com diferentes tipos de cruzamento")


	## fazendo legenda
	line_up, = plt.plot([1,2,3], label='Blend Alfa', color='red')
	line_down, = plt.plot([2,3,1], label='Mediano', color='green')
	plt.legend(handles=[line_up, line_down])

	plt.grid(True)
	plt.xlabel("Gerações")
	plt.ylabel("Fitness")
	plt.show()

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




x1 = leitura("blendAlfa.txt")
x2 = leitura("mediano.txt")
grafica(x1, x2)