def lingua_p (palavra):
    '''Retorna uma palavra traduzida para a lingua do P, str->str'''
    palavra = palavra.replace('a', 'apa')
    palavra = palavra.replace('e', 'epe')
    palavra = palavra.replace('i', 'ipi')
    palavra = palavra.replace('o', 'opo')
    palavra = palavra.replace('u', 'upu')
    palavra = palavra.replace('á', 'ápá')
    palavra = palavra.replace('é', 'épé')
    palavra = palavra.replace('í', 'ípí')
    palavra = palavra.replace('ó', 'ópó')
    palavra = palavra.replace('ú', 'úpú')
    palavra = palavra.replace('ã', 'ãpã')
    palavra = palavra.replace('õ', 'õpõ')
    return palavra