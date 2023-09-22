def lingua_p(palavra):
    '''Traduz uma palavra em português para sua correspondente na 'língua do p'.
    str --> str'''
    
    vogais = 'AÁÃÂEÉÊIÍOÓÔUÚaáãâeéêiíoóôuú'
	palavra_traduzida = ''

    for i in palavra:
        if i in vogais:
            palavra_traduzida = palavra_traduzida + i + 'p'+ i
		else:
            palavra_traduzida = palavra_traduzida + i

    return palavra_traduzida