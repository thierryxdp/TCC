def lingua_p(palavra):
    '''recebe uma palavra e retorna a mesma palavra traduzida para a íngua do P; str->str'''
    lista=list(palavra)
    for n in len(palavra):
        if lista[n] in 'aeiouAEIOU':
            lista[n+1:n+1]='p'
    return str.join('',lista)