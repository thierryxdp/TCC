def uppCons(frase):
    """recebe como entrada uma frase e retorna 
    a frase com todas as consoantes maiusculas.
    str->str"""
    nova_frase =''
    i = 0
    while i<len(frase):
    letraava=frase[i]
        if frase[i] in 'AEIOUaeiou':
            nova_frase=nova_frase+letraava
        else:
            letramai=str.upper(letraava)
            nova_frase=nova_frase+letramai
    i=i+1
    return nova_frase