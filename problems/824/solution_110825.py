def uppCons(frase):
    " " "Recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas;str, -> str " " "
    i = 0
    texto = ''
    while i<len(frase):
        if frase[i] in 'bcddfghjklmnpqrstvwxyzç':
            texto = texto + frase[i].upper()
            i = i + 1
        else:
            texto = texto + frase[i]
            i = i + 1
    return texto