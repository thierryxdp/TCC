def uppCons(frase):
    """recebe como entrada uma frase e retorna 
    a frase com todas as consoantes maiusculas.
    str->str"""
    nova_frase=''
    i=0
    while i<len(frase):
        if frase[i] in 'aeiou':
            nova_frase+frase[i]
        else:
            letramai=str.upper(frase[i])
            nova_frase+letramai
    i+=1
    return nova_frase