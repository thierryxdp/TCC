def lingua_p (palavra):
    '''Retorna uma palavra traduzida para a lingua do P, str->str'''
    palavra = palavra.replace('a', 'apa')
    palavra = palavra.replace('e', 'epe')
    palavra = palavra.replace('i', 'ipi')
    palavra = palavra.replace('o', 'opo')
    palavra = palavra.replace('u', 'upu')
    return palavra