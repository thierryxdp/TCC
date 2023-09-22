def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase, porém com todas
    as suas consoantes em maiúsculas;str->str"""
    contador=0
    nova=''
    while contador<len(frase):
        if ('A' or 'a' or 'E' or 'e' or 'I' or 'i' or 'O' or 'o' or 'U' or 'u')not in frase[contador]:
            nova=nova+str.upper(frase[contador])
        elif ('A' or 'a' or 'E' or 'e' or 'I' or 'i' or 'O' or 'o' or 'U' or 'u')in frase[contador]:
            nova=nova+frase[contador]
        contador=contador+1
    return nova