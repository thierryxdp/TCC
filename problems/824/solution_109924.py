#---------------------EXERCICIO 2---------------------

def uppCons(frase):
    '''Retorna a frase com todas as consoantes maiúscula
       str -> str'''
    
    i=0     			#contador
    frase_nova = ''     #acumulador
    
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase_nova += str.upper(frase[i])
        else:
            frase_nova += frase[i]
        i += 1
    
    return frase_nova