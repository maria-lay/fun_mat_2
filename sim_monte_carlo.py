""" SIMULAÇÃO DE MONTE CARLO"""
import random as rd
import math


# função para saber se o ponto está dentro ou fora
def teste(x, y):
    # Coordenada do centro = (1,1)
    raio = 1
    dist = math.sqrt((x - 1) ** 2 + (y - 1) ** 2)
    if dist <= raio:
        return True
    else:
        return False


# contador
dentro = 0

# quantidade de pontos
n = 1000000

# gerar pontos
for k in range(n):
    X = rd.uniform(0, 2)
    Y = rd.uniform(0, 2)

    # Verificar se está dentro ou fora
    if teste(X, Y):
        dentro += 1

# Valor obtido para área
print(4 * dentro / n)
