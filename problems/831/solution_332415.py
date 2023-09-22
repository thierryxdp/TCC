def lingua_p(palavra):
    '''
    	Funcao recebe uma palavra e "traduz" ela para a lingua do p,
        colocando, a pois toda a vogal da palavra, a letra "p" e a 
        proria vogal.
        str -> str
    '''
    palavra_p = ''
    for x in range(len(palavra)):
    	if palavra[x] in 'aáâãeéêiíoóôõuúû':
            palavra_p = str.join('',[palavra_p,palavra[x],'p',palavra[x]])
        else:
        	palavra_p = str.join('',[palavra_p,palavra[x]])
    return palavra_p