def melhor_volta(result):
    '''função que retorna o melhor tempo entre as provas; matriz => tupla'''
    melhor=[]
    for corredor in result:
        list.append(melhor,min(corredor))
    b=min(melhor)
    a=list.index(melhor,b)
    c=list.index(result[a],b)
    return (a+1,b,c+1)