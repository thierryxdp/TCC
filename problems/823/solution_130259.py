def faltante(lista):
    """Função que recebe uma lista com N-1 inteiro e retorna o número inteiro deste intervalo.
    Use list -> int: [1, 2, 3, 5] -> 4"""
    contador = 1
    resultado = 0
    #Estrutura de repetição e condicional.
    while contador <= len(lista):
        if contador not in lista:
            resultado += contador
        contador = lista[contador-1]+1
    #Condicional que completa a lista crescente com o sucessor do último valor.
    if resultado == 0:
        resultado += len(lista)+1
    return resultado