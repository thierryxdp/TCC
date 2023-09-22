def uppCons (fraseDada):
"""funcao que recebe uma frase como entrada e retorna a frase com as consoantes todas maiusculas"""
    s = " "
    for letra in fraseDada:
        if letra in "bcdfghjklmnpqrstvxwyz":
            s += letra.upper() 
        else: 
        s += caractere
    return s