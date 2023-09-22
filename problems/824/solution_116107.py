def uppCons(frase):
    """função que recebe uma frase e retorna ela com todas as consoantes em maiúsculo
    str->str""" 
    fras= str.upper(frase)
    n=0
    while n<len(fras):
        n=n+1
        if 'A' in fras:
        	str.replace(fras,'A','a')
        if 'E' in fras:
            str.replace(fras,'E','e')
        if 'I' in fras:
            str.replace(fras,'I','i')
        if 'U' in fras:
            str.replace(fras,'U','u')
        if 'O' in fras:
            str.replace(fras,'O','o')
    return fras