def primo(numero):
    """dada uma função com um numero inteiro positivo, verifica se este é ou não numero primoe esta função deve
me retornar valor um booleano. int->bool"""
    
    i=1
    lista=[]
    
    while i<=numero:
        if numero%i==0:
            lista=lista+[i]
            i=i+1
        else:
            i=i+1
    if len(lista)==2:
        return True
    else:
        return False