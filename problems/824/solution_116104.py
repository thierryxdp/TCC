def uppCons(frase):
    """função que recebe uma frase e retorna ela com todas as consoantes em maiúsculo
    str->str""" 
    str.upper(frase)
    n=0
    while n<len(frase):
        n=n+1
        if 'A' in frase:
        	str.replace(frase,'A','a')
        if 'E' in frase:
            str.replace(frase,'E','e')
        if 'I' in frase:
            str.replace(frase,'I','i')
        if 'U' in frase:
            str.replace(frase,'U','u')
        if 'O' in frase:
            str.replace(frase,'O','o')
    return frase