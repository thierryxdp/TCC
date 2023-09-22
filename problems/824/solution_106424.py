def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if frase[indice]!='U' and frase[indice]!='O' and frase[indice]!='I' and frase[indice]!='E' and frase[indice]!='A' and frase[indice]!='u' and frase[indice]!='o' and frase[indice]!='i' and frase[indice]!='e' and frase[indice]!='a':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        else:
            indice+=1
    return reformed