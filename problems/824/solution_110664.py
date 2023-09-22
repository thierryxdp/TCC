def uppCons(frase):
    '''Recebe um frase como entrada e retorna a frase
    com todas as suas consoantes em maiúsculas(e os demais
    caracteres exatamente como estavam na frase original)
    str -> str'''
    
    frase_f=''
    i=0
    
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase_f= frase_f+ str.upper(frase[i])
        else:
            frase_f= frase_f+ frase[i]
        i=i+1
    return frase_f