def posLetra(frase, letra, n):
    ''' A função recebe uma frase, uma letra, um numero e retorna a posição
        de uma ocorrencia n(1 para primeira, 2 para segunda...) de uma letra
        dentro da frase. Se a ocorrencia indicada for maior do que a existente
        o numero -1 sera mostrado.
        str, str, int -> int''' 
    posicoes = []
    i = 0
    while i <= len(frase)-1:
        if letra == frase[i]:
            list.append(posicoes, i)
        i = i +1
    if n > len(posicoes):
        return -1
    else:
        return posicoes[n-1]