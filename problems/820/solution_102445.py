def posletra(frase,letra,n):
    "recebe uma frase, uma letra e um numero inteiro n"
    "retorna a posição da ocorrência n, da letra escolhida"
    "entrada : Str,Str,Int. Saida: int."
    posição = frase.find(letra)
    while posição >= 0 and n > 1:
        posição = frase.find(letra, posição + 1)
        n -= 1
    return posição