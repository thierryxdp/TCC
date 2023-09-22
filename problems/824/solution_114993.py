def uppCons(frase):
    '''
    retorna todas as consoantes maiusculas
    str -> str
    '''
    i=0
    palavra=''
    while i<len(frase):
        if 'a' not in frase[i] and 'e' not in frase[i] and 'i' not in frase[i] and 'o' not in frase[i] and 'u' not in frase[i]:
            palavra=palavra+frase.upper(i)
            i=i+1
    return frase