#---------------------EXERCICIO 4---------------------

def maiores(lista_inteiros,n):
    '''Retorna todos os numeros maiores que n
       list,int-> list'''

    novaLista = lista_inteiros[:]
    list.append(novaLista,n)
    list.sort(novaLista)
    posicao=list.index(novaLista,n)
    
    return novaLista[posicao+1:]