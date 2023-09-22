def soma_h(n: int) -> float:
    """Calcula o valor de uma função chamada H com "n" termos

       Parameters:
       n: Número inteiro de termos a serem usados na função H

       Return:
       Dado o parâmetro "n", retorna o valor da função H com precisão de duas
       casas decimais, no qual a função H é dada por:
                    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

       Examples:
       soma_h(1) == 1.0
       soma_h(2) == 1.5
       soma_h(10) == 2.93
    """

    numeros = list(range(1, n + 1))
    resultado = 0

    for numero in numeros:
        resultado = resultado + (1 / numero)

    return round(resultado, 2)