def uppCons(frase):
    """recebe como entrada uma frase e retorna 
    a frase com todas as consoantes maiusculas.
    str->str"""
    nova_frase =''
    i = 0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            letramai = str.upper(frase[i])
            str.replace(frase,frase[1],letramai)
    i=i+1
    return