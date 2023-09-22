def lingua_p(palavra):
    '''Retorna a palavra inserida na lángua do p, com letras minúsculas;
    str -> str'''
    palavra=palavra.lower()
    final=''
    for i in range(len(palavra)):
        final=final+palavra[i]
        if palavra[i] in 'aeiouáéíóúãõâêîôû':
            final=final+'p'+palavra[i]
	return final