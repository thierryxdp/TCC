def uppCons(frase):
    '''Recebe uma frase e retorna a mesma frase com as consoantes em maiúsculas e os demais caracteres exatamente na como estavam na frase original;str->str'''
    indice=0
    while indice<len(frase):
        if 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U' in frase[indice]:
            indice+=1
        else:
          	f=frase.replace(frase[indice],str.upper(frase[indice]))
            indice+=1
    return f