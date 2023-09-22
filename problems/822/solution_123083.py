def repetidos (lista_numeros: list) -> int:
    """Recebe uma lista de números e retorna quantas vezes dois números
    iguais apareceram um, exatamente, após o outro, nesta lista."""
    posicao = 1
    contador = 0
    tamanho_da_lista = len(lista_numeros)
    while posicao < tamanho_da_lista:
        if lista_numeros[posicao] == lista_numeros[posicao - 1]:
            contador += 1
    	posicao += 1
   	return contador