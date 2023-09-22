def lingua_p(palavra):
    '''função que retorna a palavra intercalada com p; str => str'''
    p="
    for letra in palavra:
        p+=letra
        if letra in 'aáãàâeéèêiíìoòóôõuúù':
        p+='p'+letra
    return p