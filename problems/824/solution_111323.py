def uppCons(frase):
    """Recebe como entrada uma frase e retorna a mesma frase, porém com todas
    as suas consoantes em maiúsculas;str->str"""
    contador=0
    nova=''
    while contador<len(frase):
        if not('A'in frase[contador] or 'a'in frase[contador] or 'E'in frase[contador] or 'e'in 
        frase[contador] or 'I'in frase[contador] or 'i'in frase[contador] or 'O'in 
        frase[contador] or 'o'in frase[contador] or 'U'in frase[contador] or 'u'in 
        frase[contador] or 'Á'in frase[contador] or 'á'in frase[contador] or 'Ã'in
        frase[contador] or 'ã'in frase[contador]or 'É'in frase[contador] or 'é'in frase[contador] or 'Í'in
        frase[contador] or 'í'in frase[contador] or 'Ú'in frase[contador] or 'ú'in
        frase[contador] or 'Ó'in frase[contador] or 'ó'in frase[contador] or 'Õ'in
        frase[contador] or 'õ'in frase[contador]):
            nova=nova+str.upper(frase[contador])
        else:
            nova=nova+frase[contador]
        contador=contador+1
    return nova