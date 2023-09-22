def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if 'a' in frase[indice]:
            indice+=1
        elif 'e' in frase[indice]:
            indice+=1
        elif 'i' in frase[indice]:
            indice+=1
        elif 'o' in frase[indice]:
            indice+=1
        elif 'u' in frase[indice]:
            indice+=1
        elif 'A' in frase[indice]:
            indice+=1
        elif 'E' in frase[indice]:
            indice+=1
        elif 'I' in frase[indice]:
            indice+=1
        elif 'O' in frase[indice]:
            indice+=1
        elif 'U' in frase[indice]:
            indice+=1
        else:
            strin=str.upper(frase[indice])
            indice+=1
    return frase.replace(frase[indice],string)