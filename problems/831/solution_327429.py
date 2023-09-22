def lingua_p(palavra):
    '''Traduz para a lingua do p, dada uma palavra
    str ->str'''
    palavra = list(palavra)
    mensagem = ''
    i = 0
    while i < len(palavra):
        if palavra[i] in 'aeiouúéáê':
            palavra[i] += 'p' + palavra[i]
            mensagem += palavra[i]
            i += 1
            
        else:
            
            mensagem += palavra[i]
			i += 1
    
        	
    return mensagem