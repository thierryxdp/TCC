def posLetra(frase,letra,n):
    "recebe uma frase, uma letra e um numero inteiro n"
    "retorna a posição da ocorrência n, da letra escolhida"
    "entrada : Str,Str,Int. Saida: int."
    posicao = frase.find(letra)
    while posicao >= 0 and n > 1:
        posicao = frase.find(letra, posicao + 1)
        n -= 1
    return posicao