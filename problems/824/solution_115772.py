def uppCons(frase):
    "Recebe uma frase e retorna todas as suas consoantes em maiúsculo; str -> str"
    x = 0
    tamanho = len(frase)
    frase2 = ''
    vogais = '-,aeiou áéíóúâêîôûãàõ.!?:;}{[]'
    while x < tamanho:
        if frase[x] in vogais:
            frase2 = frase2+frase[x]
        else:
            letra = frase[x]
            frase2 = frase2+letra.upper()
        x = x + 1
    return frase2