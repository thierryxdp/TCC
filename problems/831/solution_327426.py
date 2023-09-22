def lingua_p(palavra):
    palavra = list(palavra)
    mensagem = ''
    i = 0
    while i < len(palavra):
        if palavra[i] in 'aeiouú':
            palavra[i] += 'p' + palavra[i]
            mensagem += palavra[i]
            i += 1
            
        else:
            
            mensagem += palavra[i]
			i += 1
    
        	
    return mensagem