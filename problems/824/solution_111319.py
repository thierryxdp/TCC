def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase, porém com todas
    as suas consoantes em maiúsculas;str->str"""
    contador=0
    nova=''
    while contador<len(frase):
        if ('A'not in frase[contador] or 'a'not in frase[contador] or 'E'not in frase[contador] or 'e'not in frase[contador] or 'I'not in frase[contador] or 'i'not in frase[contador] or 'O'not in frase[contador] or 'o'not in frase[contador] or 'U'not in frase[contador] or 'u'not in frase[contador]):
            nova=nova+str.upper(frase[contador])
        else:
            nova=nova+frase[contador]
        contador=contador+1
    return nova