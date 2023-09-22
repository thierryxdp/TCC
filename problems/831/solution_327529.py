def lingua_p(palavra):
    '''A partir de uma palavra retorna ela na \'lingua do p\'
    ou seja apos cada vogal e adicionado a letra p + a vogal.
    str -> str'''
    indice = 0
    for letra in palavra:
        if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            palavra = palavra[0:(indice+1)] + 'p' + palavra[indice:]
            indice = indice + 3
        else:
            indice += 1
    return str.lower(palavra)