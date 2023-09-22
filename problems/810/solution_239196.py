def inverte(x):
    '''função da frase retorne outra frase que contanha as mesmas palavras da frase de entrada
    em ordem inversa, sem letras maiúculas e sem pontuação:
    str -> str'''
    A = x.replace("."," ")
    B = A.replace("!"," ")
    C = B.replace(","," ")
    D = C.replace("-"," ")
    E = D.replace("?"," ")
    F = str.split(E)
    G = F[-1:-(len(F)+1):-1]
    H = str.join(" ",G)
    return str.lower(H)