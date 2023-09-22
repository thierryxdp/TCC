def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U' in frase[indice]:
            indice+=1
        else:
            strin=str.upper(frase[indice])	
          	f=frase.replace(frase[indice],strin)
            indice+=1
    return f