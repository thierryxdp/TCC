def lingua_p(palavra):
    '''Recebe como parametro uma palavra e retorna esta mesma
    palavra traduzida para a língua do P.
    string -> string'''
    lingua_p = ''
    palavra = palavra.lower()
    for i in palavra:
        if i in 'aeiou':
        	palavra += i + 'p' + i
        else:
            palavra += i
    return palavra