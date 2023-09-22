def primo(numero):
    '''Dada um numero inteiro positivo, a função verifica se
    o numero é positivo ou não, retornando um valor booleano.
    int->bool'''
    
    indice=1
    lista=[]
    
    while indice<=numero:
        if numero%indice==0:
            lista=lista+[indice]
            indice=indice+1
        else:
            indice=indice+1
    if len(lista)==2:
        return True
    else:
        return False