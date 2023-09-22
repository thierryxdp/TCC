def uppCons(frase):
    """Recebe uma frase como entrada e retorna a frase com suas consoantes
maiúsculas;
str -> str"""
    proximo = 0
    nova_frase = ""
    while proximo < len(frase):
        if frase[proximo] not in "AEIOUaeiou":
            nova_frase = nova_frase + str.upper(frase[proximo])
        else:
            nova_frase = nova_frase + frase[proximo]
        proximo = proximo + 1
    return nova_frase