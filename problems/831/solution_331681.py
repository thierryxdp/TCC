def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma 
    palavra traduzada para a lingua do P.
    string -> string'''
    palavra = palavra.lower()
    lingua_p = ''
    for i in palavra:
        lingua_p = i + 'p'
    return lingua_p