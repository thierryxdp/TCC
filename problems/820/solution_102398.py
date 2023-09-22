def posLetra (frase,letra,numero):
    "função que recebe uma frase, uma letra e um número e retorna a posicao (inteiro) da letra da string na sua n ocorrencia (número)"
    posicao = 0
    total = str.count(frase,letra)
    contagem = 0
    if 0 < numero <= total:
        if numero == 1:
            return str.find(frase,letra)
        else:
            while contagem != numero:
                if frase[posicao] == letra:
                    contagem += 1
                    if numero == contagem:
                        return posicao
            posicao += 1
    else:
        return -1