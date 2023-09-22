def posLetra(texto, letra, n):
    """Funcao recebe retorna qual a posicao que a letra escolhida: letra
    se econtra na string dada: texto, de acordo com a ocorrencia desejada
    dada: n se a letra ocorre menos vezes do que n, deve retornar -1 """

    contador = 0
    ocorrencia = 0
    
    if texto.count(letra) < n:
        return -1
    else:
        while contador < len(texto):
            if texto[contador] != letra:
                contador += 1
            elif texto[contador] == letra and (ocorrencia+1) == n:
                return contador
            else:
                contador += 1
                ocorrencia += 1