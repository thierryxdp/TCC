def faltante(lista_de_numeros):
    """funcao que retorna a numeracao da peca que esta faltando;
    list de int -> int"""
    i=0
    if 1 not in lista_de_numeros:
        return 1
    while i<len(lista_de_numeros):
        if lista_de_numeros[i]+1 not in lista_de_numeros:
            return lista_de_numeros[i]+1
        i=i+1