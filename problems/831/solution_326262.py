def lingua_p(palavra):
    '''retorna a palavra traduzida para a lingua do P. string->string'''
    lista=list(palavra)
    n=0
    for i in lista:
        if i in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            list.insert(lista,n,'p'+i)
            n=n+1
    return str.join('',lista)