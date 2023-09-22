def lingua_p(palavra):
    '''Recebe uma palavra e retorna esta mesma 
    palavra traduzada para a lingua do P.
    string -> string'''
    palavra = palavra.lower()
    lingua_p = []
    for i in palavra:
        lingua_p.append(i + 'p'[i+1])
    return lingua_p