#---------------------EXERCICIO 4---------------------

def maiores(lista_inteiros,n):
    '''Retorna todos os numeros maiores que n
       list,int-> list'''

    novaLista = lista_inteiros[:]
    list.append(novaLista,n)
    list.sort(novaLista)
    posicao=list.index(novaLista,n)
    
    return novaLista[posicao+1:]

#---------------------EXERCICIO 5---------------------

def acima_da_media(lista_notas):
    '''Retorna todas as notas(menor para maior),
        que ficaram acima da média
       list,int-> list'''

    media = sum(lista_notas)/len(lista_notas)
    maioresNotas = maiores(lista_notas,media)
    
    return maioresNotas