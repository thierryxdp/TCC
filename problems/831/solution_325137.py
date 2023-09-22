def lingua_p(palavra):
    '''recebe uma palavra e retorna a mesma palavra traduzida para a íngua do P; str->str'''
    lista=list(palavra)
    i=len(palavra)
    for n in range(i):
        if lista[n] in 'aeiouAEIOU':
            list.insert(lista,n,'p')
    return str.lower(str.join('',lista))