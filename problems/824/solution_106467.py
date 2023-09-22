def uppCons(frase):
    '''funcao que dado a frase retorna todas
    as consoantes em maiusculo e o resto da 
    frase permanece igual; str->str'''
    
    i = 0
    while i < len(frase):
        if frase[i] not in 'aeiouAEIOU':
            str.upper(frase[i])
         i = i + 1
    return frase