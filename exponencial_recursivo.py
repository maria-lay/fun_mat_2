# Implementação de exponencial recursivo

# Definição da função exponencial:
def exp_recursivo(base, expoente):
    if expoente < 0:
        return 1
    return base * exp_recursivo(base, expoente - 1)


def main():
    # Entradas da base e potência:
    print('-' * 40)
    base = int(input('Informe a base da exponenciação: '))
    expoente = int(input('Informe o expoente da exponenciação: ')) - 1
    # Saída de dados:
    print('-' * 40)
    print("{} elevado a {} é igual a {}".format(base, expoente, exp_recursivo(base, expoente)))


if __name__ == '__main__':
    main()
