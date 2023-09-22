def uppCons(frase):
    """ Recebe uma frase e retorna a frase com todas as suas consoantes em
    maiúsculas
    str -> str
    """
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] not in "AEIOUaeiouãáàâóíéú":
            nova_frase += str.upper(frase[i])
        else:
            nova_frase += frase[i]
        i+=1
    return nova_frase