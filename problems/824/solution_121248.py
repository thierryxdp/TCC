def uppCons(frase):
    a=[]
    for i in range(len(frase)):
        if frase[i]=='abcdeABCDE':
            a.append(frase[i])
        else:
            a.append(str.upper(frase[i]))
    return a