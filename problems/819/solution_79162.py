def filtraMultiplos(lista_de_numeros,numero):
    """funcao que retorna uma lista com todos os elementos da lista de entrada, que sejam divisível por algum numero;
    list de float, float -> list de float"""
    i=0
    lista_de_multiplos=[]
    
    while i<len(lista_de_numeros):
        if lista_de_numeros[i]%numero==0:
            lista_de_multiplos=lista_de_multiplos+[lista_de_numeros[i]]
        i=i+1
    return lista_de_multiplos