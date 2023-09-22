def lingua_p(palavra):
    '''recebe uma palavra e retorna a mesma palavra traduzida para a íngua do P; str->str'''
    lista=list(palavra)
    i=len(palavra)
    for n in range(i+1):
        if lista[n] in 'aeiouAEIOU':
            list.insert(lista,n+1,'p'+lista[n])
    return str.lower(str.join('',lista))