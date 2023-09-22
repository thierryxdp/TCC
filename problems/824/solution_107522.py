def uppCons(frase):
    """Funcap que recebe uma frase e retorna esta frase com todas as suas consoantes em maiusculas;st->str"""
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.replace(frase,frase[i],str.upper(frase[i]),)
        i=i+1
    return frase