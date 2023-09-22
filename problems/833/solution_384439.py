# QUESTÃO 2 - OK!
def conta_numero(numero,matriz):
    """ Dado um numero e uma matriz(tamanho qualquer) vamos retornar qual a quantidade de ocorrencias desse numero.
        Parametros:
        Entrada -> numero,matriz : int,list
        Saida   -> int """
    m=matriz
    ocor=0 #Ocorrencias
    if matriz==[]:
        return 0
    num_linha=len(m)
    num_coluna=len(m[0])
    for i in range(num_linha):
        for j in range(num_coluna):
            if m[i][j]==numero:
                ocor=ocor+1
    return ocor

conta_numero(0,[[1,0],[1,1]])