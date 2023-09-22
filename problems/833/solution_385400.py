def conta_numero(inteiro,matriz):
    "dada um inteiro e uma matriz, retorna as repeticoes do inteiro na matriz"
    contagem = 0
    for linha in matriz:
        for numero in linha:
            if numero == inteiro:
                contagem += 1
    return contagem