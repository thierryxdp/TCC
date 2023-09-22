#---------------------EXERCICIO 2---------------------

def conta_numero(numero,matriz):
    '''Retorna quantos numeros igual ao inserido há na matriz
       int,list -> int'''
    contador = 0 #conta a quantidade de repeticoes do numero na matriz
    for contaLinha in range(len(matriz)):
        for contaColuna in range(len(matriz[contaLinha])):
            if matriz[contaLinha][contaColuna] == numero:
                contador += 1
    return contador