def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if frase[indice]=='a':
            indice+=1
        elif frase[indice]=='e':
            indice+=1
        elif frase[indice]=='i':
            indice+=1
        elif frase[indice]=='o':
            indice+=1
        elif frase[indice]=='u':
            indice+=1
        elif frase[indice]=='A':
            indice+=1
        elif frase[indice]=='E':
            indice+=1
        elif frase[indice]=='I':
            indice+=1
        elif frase[indice]=='O':
            indice+=1
        elif frase[indice]=='U':
            indice+=1
        else:
            string=str.upper(frase[indice])
            reformed=frase.replace(frase[indice],string)
            indice+=1
    return reformed