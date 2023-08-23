"""
Uma empresa seleciona entre 10 candidatos, a cada ano, profissionais para contratá-los. No teste de seleção, existe igual chance de aprovação ou reprovação(50%). Se um candidato for reprovado pela primeira vez, ele terá outra chance e fará um novo teste. A longo prazo (vários anos) qual será o percentual de aprovados?

Mais informações sobre o problema

● Note que para cada candidato haver ́a no m ́aximo duas simulações;

● Para ser reprovado em definitivo, um candidato precisa ser reprovado duas vezes seguidas;

● Simule 10 candiatos para um número N de anos para os quais a seleção foi realizada;

● Ao final dos N anos, determine a o percentual de aprovados com relação ao total de candidatos;
"""

#Algortimo de Simulação para o problema de aprovados e reprovados:

import random as rd #

#Chance de ser aprovado(0.5) e reprovados(0.5)
def selecao():
  chance = rd.randint(1,100)
  if chance <= 50:  # se for aprovado ja retorna direto
    return [1,0]
  else:  # se reprovado há uma nova avaliação
    chance = rd.randint(1,100)
    if chance <= 50:  # aprovado na segunda tentativa
      return [1,0]
    else:  # reprovado de vez
      return [0,1]


def simulacao(candidatos):
  aprovados = 0
  reprovados = 0
  for k in range(candidatos):
    selecionados = selecao()  #selecionadosretornar uma lista informando se foi aprovado ou não
    aprovados += selecionados[0]
    reprovados += selecionados[1]
  return [round(aprovados/candidatos,3), round(reprovados/candidatos,3)]

# Fazer várias "anosetições" de simulacao e calcular a média dos resultados

candidatos = 10
print('-'*65)
anos = int(input("Para quantos anos você deseja verificar a simulação? "))

porcentagens = [0,0]
for k in range(anos):
  porcentagens[0] += simulacao(candidatos)[0]
  porcentagens[1] += simulacao(candidatos)[1]

media_aprovados = round(porcentagens[0]* 100/anos,2)
media_reprovados = round(porcentagens[1]* 100/anos,2)


print(f'Para {anos} anos temos os seguintes dados: ')
print(f"Aprovados = {media_aprovados}%")
print(f'Reprovados = {media_reprovados}%')
