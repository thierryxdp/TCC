def lingua_p(palavra):
    '''Função que recebe uma palavra qualquer e retorna a mesma traduzida para a língua do p;
    str -> str'''
    palavra_p = []
    for letra in palavra:
        if letra in 'aeiouAEIOUáéíóú':
            palavra_p = palavra_p + list(letra) + list('p') + list(letra)
        else:
            palavra_p = palavra_p + list(letra)
    return (''.join(palavra_p))