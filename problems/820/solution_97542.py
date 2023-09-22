def posLetra(frase,letra,n):
    " " "Recebe como entra uma frase, uma letra e um numero que indica a posição desejada da letra,retorna em que posição da frase a letra está; str, str, int, -> int " " "
    i = 0
    inicio = 0
    resposta = 0
    while i<n:
        inicio = str.find(frase,letra,inicio) + 1
        resposta = inicio -1
        i = i + 1
    return resposta