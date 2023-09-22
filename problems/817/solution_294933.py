def maiores(lista,n):
    '''Retorna uma lista de numeros maiores que n, baseada
       na lista dada como argumento;
       list, int -> list'''
    
    lista.append(n)
    lista.sort()
    ind = lista.index(n)
    
    return lista[ind+1:]

def acima_da_media(notas):
    '''Função que dada a lista das notas de uma turma
       retorna a lista das notas acima da média;
       list -> list'''
    
    media = sum(notas) / len(notas)
    
    notas_maiores = maiores(notas,media)
    
    return notas_maiores