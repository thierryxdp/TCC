# Lingua do P

def lingua_p(palavra):
    '''Dada uma palavra em portugues, retorna a mesma palavra traduzida para a lingua do P.
    str -> str'''
    palavra_em_p = ''
    for caractere in palavra.lower():
        if caractere in 'aeiouãõáé':
            palavra_em_p += caractere + 'p' + caractere
        else:
            palavra_em_p += caractere
    return palavra_em_p