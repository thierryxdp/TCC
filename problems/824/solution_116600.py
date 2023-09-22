def uppCons(frase):
    '''Funçao que, fornecida uma frase, retorna a própria, com
    todas as suas consoantes em maiúsculas, deixando o restante
    na forma original
    str -> str
    '''
    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase2, str.upper(frase[i]))
        else:
            list.append(frase2, frase[i])
        i = i + 1
    return str.join("", frase2)