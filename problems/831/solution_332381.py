def lingua_p(palavra):
    '''
    Função que recebe uma palavra e retorna está mesma palavra na lingua do P.
    str-> str
    '''
    x=str.lower(palavra)
    i=0
    palavraP=''
    while i<len(x):
        if x[i] not in "aeiouáéú":
            palavraP=palavraP+x[i]
        
        else:
            palavraP=palavraP+x[i]+"p"+x[i]
        i=i+1
    return palavraP