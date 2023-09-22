def filtrarMultiplos(lista_numeros,n):
    """
    Função que retorna os multiplos de n que estam na
    lista_numeros.
    Parâmetro de Entrada: list, int
    Valor de Saida: list
    """
    
    lista_multiplos=[]
    i=0
    
    while i<len(lista_numeros):
        if lista_numeros[i]%n==0:
            list.append(lista_multiplos,lista_numeros[i])
        i=i+1
    return lista_multiplos