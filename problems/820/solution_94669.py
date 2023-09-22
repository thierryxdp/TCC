# Dada uma frase, uma letra e o número da ocorrência n, esta função retorna o
# índice da posição da ocorrência n da letra informada na frase em questão.
# Caso a quantidade de ocorrências informada seja menor do que a quantidade real,
# a função retornará -1.
# str, str, int -> int


def posLetra(frase, letra, ocorrencia):
    cont = 0
    i = 0
    while i<len(frase):
        if frase[i] == letra:
            cont = cont + 1
            if cont == ocorrencia:
                resposta = i
        i = i+1
    if cont<ocorrencia:
        resposta = -1
        
    return resposta