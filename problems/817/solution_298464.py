def maiores(lista,n):
    '''funcao que dada uma lista de inteiros e um numero inteiro n, retorna outra lista com 
    todos os numeros maiores que n ordenados em ordem crescente
    list,int->list
    '''
    lista.append(n)
    lista.sort()
    x=lista.index(n)
    lista.remove(n)
    if x==x+1
    	return lista[x+1:]
    else:
        return lista[x:]
def acima_da_media(lista):
    media=sum(lista)/len(lista)
    return maiores(lista,media)