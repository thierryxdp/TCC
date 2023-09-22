def conta_frases(s):
    "funcao que recebe texto e retorna o numero de frase no texto"
    #str -> int

    char=['!','?','.',',']
    texto= s.split()
    cont= 0
    for lac_pal in texto:
        for lac_char in char:
            if lac_char in lac_pal:
                cont+=1
                return cont