def eh_consoante(letra):
    return letra.lower() in 'bcdfghjklmnpqrstvwxyzç'

def uppCons(frase):
    ''' Retorna as consoantes da frase em maiúsculas, 
    e os demais sem alteração.
    str --> str'''
    
    nova_frase = ''
    
    i = 0
    while i < len(frase) :
		letra = frase[i]
        
        if eh_consoante(letra):
			letra = str.upper(letra)
		
		nova_frase += letra
        
        i += 1
    
    return nova_frase