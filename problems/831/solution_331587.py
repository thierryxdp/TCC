def lingua_p(palavra):
    ''' Traduz uma palavra para a língua P
    str -> str'''
    
    nova_palavra = ''
    for i in range(len(palavra)):
        if not palavra[i].lower() in 'aeiou':
            nova_palavra += palavra[i] + 'p'
        else:
            nova_palavra += palavra[i]
	return nova_palavra