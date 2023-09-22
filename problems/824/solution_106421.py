def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if frase[indice]!='a':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='e':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='i':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='o':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='u':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='A':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='E':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='I':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='O':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        elif frase[indice]!='U':
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
        else:
            indice+=1
    return reformed