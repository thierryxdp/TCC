def quant_palavras(frase):
#essa função recebe uma frase e retorna quantas palavras ela possui
#string -> int
    frase = frase.strip()
    frase = frase.split()

    return len(frase)