def repetidor(lista):
    '''Função que retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list->int'''
    i=1
    x=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            x=x+1
   	i=i+1
return x