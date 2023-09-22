def repetidos(l):
    '''Função que recebe como entrada uma lista de números e retorna
    	o número de vezes que um elemento da lista é igual ao elemento
        anterior'''
    i=0
    a=0
    while i<len(l)-1:
        if l[i+1]==l[i]:
            a=a+1
        i=i+1
    return a