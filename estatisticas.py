import statistics
## código responsável por fazer média, desvio padrão de nossos valores
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



info = leitura("saida1.txt")

media = statistics.mean(info)
dp = statistics.stdev(info)
print("Média ", media)
print("Desvio padrão ", dp)