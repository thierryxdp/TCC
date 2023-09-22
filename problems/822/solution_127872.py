def repetidos(x):
    '''
    função que recebe como entrada uma lista de números e retorna o número de vezes que um 
    elemento da lista é igual ao elemento anterior.
    list-> int
    '''
    lista= []
    i = 0
    while i<len(x):
        if x[i]==x[i+1]:
            lista=lista+[1]
        i=i+1
    return sum(lista)