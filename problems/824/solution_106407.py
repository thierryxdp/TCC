def uppCons(frase):
    '''recebe como entrada uma frase e retorna a mesma frase com as consoantes maiúsculas; str->str'''
    i=0
    while i<len(frase):
        if 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U' in frase[i]:
            i=i+1
        else:
            z=str.upper(frase[i])
            k=str.replace(frase, frase[i], z)
      		i=i+1
    return k