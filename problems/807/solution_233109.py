def conta_frases(s):
    "recebe texto e retorna o numero de frase no texto"
    char=['!','?','.',',']
    texto= str.split(s)
    cont= 0
    for lac_pal in texto:
        for lac_char in char:
            if lac_char in lac_pal:
                cont+=1
                return cont