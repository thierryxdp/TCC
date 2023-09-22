def inverte(x):
    '''Dada uma frase, a função inverte esta frase e retira as pontuações
    e coloca a frase em letra minúscula
    str -> str'''
    
    
    i = 0
    u = ''
    y = ['-',',',':',';','.','!','?']

    while len(x) > i:
        if x[i] not in y:
            u = u + x[i]
        if x[i] in y:
            u = u + ' '
        i = i + 1
    
    a = str.split(u)    
    v = -1
    z = ''
    
    while -(len(a)) < v:
        if a[v] in u:
            z = z + a[v]
        v = v - 1
        
    b = str.split(z)    
    return b