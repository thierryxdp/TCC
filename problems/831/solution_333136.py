def lingua_p(palavra):
    '''funçao que receba como parametro uma palavra e retorne
    esta mesma palavra traduzida para a lingua do P;
    str -> str'''
    palavra_com_p = []
    for i in palavra:
        if i in 'aáéeíióoúu':
            palavra_com_p += i+'p'+i
        else:
            palavra_com_p += i
    return str.join('',palavra_com_p)