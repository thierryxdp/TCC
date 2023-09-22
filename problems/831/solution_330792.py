def lingua_p(palavra):
    i=0
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            posicao=palavra.index(letra)
            palavra=str(palavra[0:posicao])+'p'+letra+str(palavra[posicao:1])
        i=i+1
        elif i<len(palavra):
            return palavra