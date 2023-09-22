def lingua_p(palavra):
    novapalavra = ''
    for letra in palavra:
    	novo = ''
        if letra in 'aàáâãeèéêiìíîoòóôõuùúûAÀÁÂÃEÉÈÊIÍÌÎOÒÓÔÕUÙÚÛ':
            novo = 'p' + letra
        novapalavra = novapalavra + letra + novo
    return str.lower(novapalavra)