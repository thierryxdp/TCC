def primo(n):
    '''Recebe um numero inteiro e positivo e Retorna True se ele for primo
    e False se ele nao for;
    int -> bool'''
    lista=[]
    x=list(range(1,n+1))
    for i in x:
        if n%i==0:
            lista=lista+[i]
    if len(lista)==2:
        return True
    else:
        return False