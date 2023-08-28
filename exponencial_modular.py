""" Exponencial Modular """

from math import floor


# Definindo a função exponencial modular:
def exp_mod(base, potencia, modulo):
    # definindo o caso base
    if potencia == 0:
        return 1
    # Definindo as exceções:
    elif base == 0 and potencia == 0:
        return "Impossível"
    elif modulo < 2:
        return "Impossível"
    # definindo quando n é par
    elif potencia % 2 == 0:
        return (exp_mod(base, potencia // 2, modulo)) ** 2 % modulo
    # definindo quando n é impar:
    else:
        return (((exp_mod(base, floor(potencia / 2), modulo)) ** 2 % modulo) * (base % modulo)) % modulo


def main():
    print('-' * 22)
    # Definindo as entradas
    a_base = int(input('Valor da base: '))
    n_potencia = int(input('Valor da potência: '))
    m_modulo = int(input('Valor do módulo: '))
    print('*' * 22)
    # Definindo a saída:
    resposta = exp_mod(a_base, n_potencia, m_modulo)
    print(f"O resultado é {resposta}")


if __name__ == '__main__':
    main()
