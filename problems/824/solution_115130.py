def uppCons(frase):
    """recebe como entrada uma frase e retorna 
    a frase com todas as consoantes maiusculas.
    str->str"""
    nova_frase =''
    i = 0
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            nova_frase=nova_frase+frase[i]
        print nova_frase
        else:
            letramai=str.upper(frase[i])
            nova_frase=nova_frase+letramai
        print nova_frase
    i=i+1
    return frase