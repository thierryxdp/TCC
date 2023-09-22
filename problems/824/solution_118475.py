def uppCons(x):
    '''
    função que recebe como entrada uma frase (x) e retorna a frase com todas as suas 
    consoantes em maiusculo.
    str->str
    '''
    lista=[]
    i=0
    while i<len(x):
        if x[i] not in 'aeiouãóúíé':
            lista= lista+ [str.upper(x[i])]
        else:
            lista= lista+ [x[i]]
        i = i+1
    return str.join('',lista)