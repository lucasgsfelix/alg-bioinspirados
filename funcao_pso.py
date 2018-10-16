import math

def funcaoObjetivo(x): ### x é como se fosse o individuo da função, é uma função de maximização

### função de fitness

	return (x*(math.sin(10*math.pi*x))) + 1