""" MÁXIMO DIVISOR COMUM """

# Definindo a função MDC:
def mdc(x, y):
    # Definindo as exceções:
    if x == 0 and y == 0:
        return "O mds é indeterminado"
    # Primeiro argumento seja maior que o segundo:
    elif x < y:
        x, y = y, x
    # Voltando ao caso base
    elif y == 0:
        return x
    else:
        return mdc(y, x % y)


def main():
    # Definição das entradas:
    print('-' * 36)
    print('-' * 7, 'MÁXIMO DIVISOR COMUM', '-' * 7)
    X = int(input('Informe o primeiro número: '))
    Y = int(input('Informe o segundo número: '))

    # Definindo a saída:
    print('*' * 36)
    resposta = mdc(X, Y)
    print(f'o MDC de {X} e {Y} é igual a {resposta}')


if __name__ == '__main__':
    main()
