def lingua_p(palavra):
    '''Retorna a palavra de entrada com uma letra p a cada vogal e mais a vogal, além de tornar a palavra inteiramente em minúsculas;
    str -> str'''
    lista = list(str.lower(palavra))
    linguap = [] 
    i= 0
    for i in range(0,len(lista)):
        if lista[i] in 'aeiou':
            list.append(linguap, lista[i] +'p'+lista[i])
        else:
            list.append(linguap,lista[i])
        i=i+1    
    return linguap