def uppCons(frase):
    ''' Retorna as consoantes da frase em maiúsculas, 
    e os demais sem alteração.
    str --> str'''    
    nova_frase = ''    
    i = 0
    while i < len(frase) :
		letra = frase[i]
        # se é consoante, coloque em caixa alta
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
			letra = str.upper(letra)	
		nova_frase += letra
        i += 1    
    return nova_frase