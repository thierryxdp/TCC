def uppCons(frase):
    """ Função que recebe como entrada uma frase e retorn a frase
    com todas as consoantes em maiúsculas.
    srt -> srt"""
    frase1 = frase
    for i in frase:
        if i not in "aãáeéiíoóúuAEIOU ":
          frase1 = frase1.replace(i,i.upper())
    return frase1