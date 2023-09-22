def fatorial(numero: int) -> int:
    """Dado um número, calcula o fatorial desse número

       Parameters:
       numero: Número inteiro que iremos calcular o fatorial

       Return:
       Dado o parâmetro "numero", retorna o valor do fatorial do parâmetro
       "numero"

       Examples:
       fatorial(4) == 24
       fatorial(5) == 120
       fatorial(10) == 3628800
       fatorial(0) == 1
    """

    i = 0
    resultado = 1
    lista = list(range(numero + 1))
    del lista[0]
    
    while i < len(lista):
        resultado = resultado * lista[i]
        i = i + 1

    return resultado