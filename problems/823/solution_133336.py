def faltante(lista_numeros):
    """
    Função que dada uma lista com números inteiros de 1 a N, retorna 
    qual número inteiro deste intervalo está faltando.
    Parâmetro de Entrada:list
    Valor de Saida: int
    """
    
    lista_ideal = list(range(1,lista_numeros[-1]+1))
    faltante=0
    i=0
    
    if lista_numeros!=lista_ideal:
        while i<len(lista_numeros):
            if lista_ideal[i] not in lista_numeros:
                faltante=lista_ideal[i]
            i=i+1    
        return faltante
    
    elif lista_numeros==lista_ideal:
        return lista_numeros[-1]+1