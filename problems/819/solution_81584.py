def filtraMultiplos(lista,num):
#Funcao que filtra os multiplos de um numero n
    i=0
    lista_multiplos=[]
    while i<len(lista):
        if lista[i]%num==0:
            lista_multiplos+=[lista[i]]
        i+=1
    return lista_multiplos
#Retorna outra lista com os elementos da lista original que forem divisíveis por n