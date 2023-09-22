def uppCons(frase):
    """funcao que recebe uma frase e retorna a frase com
    suas consoantes em maiúsculo, com os demais caracteres
    inalterados
    str->str"""
    fraseUppCons = ''
    i = 0
    while i < len(frase):
        caractere = frase[i]
        if caractere in 'bcçdfghjklmnpqrstvxyzw':
            caractere = str.upper(caractere)
        fraseUppCons = fraseUppCons + caractere
        i = i + 1
    return fraseUppCons