def acima_da_media(lista):
    '''função que dada uma lista com a nota de x alunos, retorna
    uma nova lista que ordena a nota dos alunos que ficaram acima
    da média.
    entrada da função: list
    saída da função: list'''

    media= sum(lista)/ len(lista)
 
    x = list.index(lista,media)
    
    if x not in lista:
        lista.append(x)
        
    y = lista[x+1:]
    
    z = y.count(media)
    
    return y[z:]