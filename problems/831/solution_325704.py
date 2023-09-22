def lingua_p(palavra):
    '''Retorna a palavra de entrada com uma letra p a cada vogal e mais a vogal, além de tornar a palavra inteiramente em minúsculas;
    str -> str'''
    lista = list(str.lower(palavra))
    l = [] 
    i= 0
    for i in range(0,len(lista)):
        if lista[i] in 'aeiouáâéêíòôú':
            list.append(l, lista[i] +'p'+lista[i])
        else:
            list.append(l,lista[i])
        i=i+1

    x = 0
    linguap = ''
    while x < len(l):
        linguap = linguap + l[x]
        x = x+1
    return linguap