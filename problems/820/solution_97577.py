def posLetra(frase, letra, n):
    "essa funcao recebe uma string,uma letra e um numero, e retorna em que posicao da string aquela ocorrencia da letra esta; str, str, int -> int"
    inicio = frase.find(letra)
    while inicio >= 0 and n > 1:
        inicio = frase.find(letra, inicio + 1)
        n -= 1
    return inicio