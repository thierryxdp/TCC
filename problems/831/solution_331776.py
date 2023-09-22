def lingua_p(palavra):
    '''Recebe como parametro uma palavra e retorna esta mesma
    palavra traduzida para a língua do P.
    string -> string'''
    lingua_p = ''
    palavra = palavra.lower()
    for i in palavra:
        if i in 'aeiou':
        	lingua_p += i + 'p' + i
        else:
            lingua_p += i
    return lingua_p