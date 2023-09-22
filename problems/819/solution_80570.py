def filtraMultiplos(lista,n):
    '''Uma função que filtra os multiplos de n que é recebido com a lista
    e retorna lista: list,int -> list'''
    i=0
    lista=[]
    listaf = lista
    while i<len(lista):
        if lista[i]%n == 0:
            lista.append[i]
        i=i+1
          return listaf