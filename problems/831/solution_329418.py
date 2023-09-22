def lingua_p(palavra):
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            posicao=palavra.index(letra)
            palavra=str(palavra[0:posicao])+'p'+letra+str(palavra[posicao:1])
            return palavra