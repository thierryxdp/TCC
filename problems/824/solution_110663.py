def uppCons(frase):
    '''Recebe um frase como entrada e retorna a frase
    com todas as suas consoantes em maiúsculas(e os demais
    caracteres exatamente como estavam na frase original)
    str -> str'''
    
    frase_f=''
    i=0
    
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase_f= frase_f+ str.upper(lista[i])
        else:
            frase_f= frase_f+ lista[i]
        i=i+1
    return frase_f