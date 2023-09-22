def primo(n):
    '''dado um número inteiro positivo, é retornado True se ele for primo e é retornado False se ele não for primo;int->boolean'''
    lista=[]
    for c in range(1,n+1):
        if n%c==0:
            lista.append(c)
    if len(lista)==2:
        return True 
    else:
        return False