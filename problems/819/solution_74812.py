def filtraMultiplos(lista_de_numeros,n):
    """Essa função filtra múltiplos do número n dado uma lista. Como
    entrada temos a lista de números e um número n, e como saída temos
    uma lista dos multiplos de n que estão contidos na lista de entrada;
    list,int->list"""
    indice=0
    lista_de_multiplos=[]
    while indice<len(lista_de_numeros):
        if lista_de_numeros[indice]%n==0:
            lista_de_multiplos= lista_de_multiplos+[lista_de_numeros[indice],]
        indice+=1
    return lista_de_multiplos