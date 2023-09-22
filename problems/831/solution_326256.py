def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P. string->string'''
    lista=list(palavra)
    for i in lista:
        if i in 'aeiouAEIOU':
            list.insert(lista,list.index(lista,i)+1,'p')
    return str.join('',lista)