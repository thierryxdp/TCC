def uppCons(frase):
    """funcao que recebe uma frase e retorna a mesma frase com suas consoantes em maiúsculas.
    str->str."""
    i=0
    str_resposta=""
    while i<len(frase):
        if frase[i] in "bcdfghjklmnpqrstvxyç":
            x=str.upper(frase[i])
            str_resposta=str_resposta+x
        else:
            str_resposta=str_resposta+frase[i]
        i=i+1    
    return str_resposta