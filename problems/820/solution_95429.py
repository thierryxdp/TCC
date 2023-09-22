'''Função que recebe uma string, uma letra e um número que indica a ocorrência 
desejada da letra e retorna em que posição da string dada a ocorrência da letra 
dada está'''
def posLetra(frase,letra,n):
    x=list(frase)
    contador = -1
    aux = 0
    booleano = False
    for l in x:
        contador += 1
        if letra == l:
            aux +=1
            if aux == n:
                booleano = True
                return contador
            else:
                continue
    if booleano == False:
            return -1