def uppCons(frase):
    """Função que dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas;
    str -> str"""

    upp_consoantes = ''
    indice = 0
    
    while (indice < len(frase)):
        if frase[indice] in "bcçdfghjklmnpqrstvwxyz":
           upp_consoantes += str.upper(frase[indice])
        if frase[indice] in "aeiouAEIOUâãàáéóõú,.:;?!-":
            upp_consoantes += frase[indice]
           
        indice += 1

    return upp_consoantes