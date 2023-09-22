def posLetra(string,letra,numero_ocor):
    """verifica se a letra esta na posição da string que é indicada com base nos valores fofornecidos na entrada
    ("string",'letra',numero) => posição"""
    posicao = str.find(string, letra)
    ocorrencia = 1 if not posicao == -1 else 0
    numero = ocorrencia
    while ocorrencia and numero < numero_ocor:
        posicao = str.find(string,letra, posicao + 1, len(string))
        numero += ocorrencia
    return (posicao)