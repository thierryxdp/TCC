def uppCons (frase):
    """retorna a frase com todas as consoantes em maiúsculas"""
    n = 0 
    frasefinal = ''
    
    while n < len(frase):
       	if str.lower(frase[n]) in 'çbcdfghjklmnpqrstvwxyz':
            maiusculo = str.upper(frase[n])
            frasefinal = frasefinal + maiusculo
            n = n + 1
            
       	elif str.lower(frase[n]) in 'aeiou': 
            minusculo = frase[n]
            frasefinal = frasefinal + minusculo
            n+=1
            
       	elif frase[n] == ' ':
            frasefinal = frasefinal + ' '
            n +=1
            
    return frasefinal