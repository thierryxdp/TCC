def lingua_p(palavra):
    '''Retorna a palavra inserida como parâmetro na lingua do p
    	str -> str'''
    novapalavra = ''
    for letra in palavra:
    	novo = ''
        if letra in 'aàáâãeèéêiìíîoòóôõuùúûAÀÁÂÃEÉÈÊIÍÌÎOÒÓÔÕUÙÚÛ':
            novo = 'p' + letra
        novapalavra = novapalavra + letra + novo
    return str.lower(novapalavra)