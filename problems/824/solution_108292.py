def uppCons(frase):
    '''Faça uma funçao que receba como entrada uma frase e retorne a frase com todas as suas consoantes em
maiúsculas (e os demais caracteres exatamente como estavam na frase original).'''
    #str > str
    a = ""
    for letra in frase:
        if letra not in "aeiouAEIOU":
            a = a + letra.upper()
        else:
            a = a + letra.lower()
    return a