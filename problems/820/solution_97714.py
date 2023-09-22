def posLetra(string,letra,numero_ocor):
    posicao = str.find(string, letra)
    ocorrencia = 1 if not posicao == -1 else 0
    numero = ocorrencia
    while ocorrencia and numero < numero_ocor:
        posicao = str.find(string,letra, posicao + 1, len(string))
        numero += ocorrencia
    return (posicao)