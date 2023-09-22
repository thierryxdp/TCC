def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase, porém com todas
    as suas consoantes em maiúsculas;str->str"""
    contador=0
    nova=''
    while contador<len(frase):
        if ('A'in frase[contador] or 'a'in frase[contador] or 'E'in frase[contador] or 'e'in frase[contador] or 'I'in frase[contador] or 'i'in frase[contador] or 'O'in frase[contador] or 'o'in frase[contador] or 'U'in frase[contador] or 'u'in frase[contador]):
            nova=nova+frase[contador]
        else:
            nova=nova+str.upper(frase[contador])
        contador=contador+1
    return nova