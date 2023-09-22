def repetidos(lista):
    '''funcao que dado uma lista de numeros,retorna o numero de vezes
    que um elemento da lista é igual ao elemento anterior'''
    i=0
    nlista=[]
    while i<len(lista):       
        if lista[i] == lista[i-1]:   
            lista.append(i)
        i=i+1
    return len(nlista)