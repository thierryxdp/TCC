def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if frase[indice] not in 'aeiouAEIOU':
            str.upper(frase[indice])
            str.replace(frase,str.upper(frase[indice],500)
            indice+=1
        else:
            indice+=1
    return frase