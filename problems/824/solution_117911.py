def vogal(x):
    '''Função que retorna True se a letra introduzida na função for uma vogal e False se for uma consoante
    str -> bool'''
    if x in 'aeiouáéíóúàãõâô':
    	return True
    else:
        return False

def uppCons(frase):
    '''Função que dado um texto retorna o mesmo com todas as consoantes em maiúsculo
    str -> str'''
    i=0
    nova=frase
    while i<len(frase):
        if vogal(frase[i])==False:
            nova=str.replace(nova,nova[i],str.upper(nova[i]),1)
        i=i+1
    return nova