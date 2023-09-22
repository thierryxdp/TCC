def uppCons(frase):
    """função que recebe uma frase e retorna ela com todas as consoantes em maiúsculo
    str->str""" 
    str.upper(frase)
    n=0
    while n<len(frase):
        n=n+1
        if 'A' in frase:
        	replace(frase,'A','a')
        if 'E' in frase:
            replace(frase,'E','e')
        if 'I' in frase:
            replace(frase,'I','i')
        if 'U' in frase:
            replace(frase,'U','u')
        if 'O' in frase:
            replace(frase,'O','o')
    return frase