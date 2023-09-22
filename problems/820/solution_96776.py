#Entrada: Uma string, uma letra e um indice
#Precisamos analisar a ocorrencia de cada letra 
#Se o indice passado for 1, a primeira vez que encontrarmos a letra 
#Devemos retornar sua posição na frase
#Se for maior, precisamos somar o numero de ocorrencias até que ele seja
#igual ao indice passado
#Caso exista menos ocorrrencias da letra do que a ocorrencia passada
#retornamos -1
def posLetra(frase: str, letra: str, n: int) -> int:
    """Recebe uma string, uma letra e um número que indica a ocorrência
    retorna a posição da letra na string de acordo com o numero de ocorrencia
    passado!"""
    i=0
    ocorrencia=0
    while i< len(frase):
        if letra == frase[i]:
            ocorrencia+=1
            if ocorrencia == n:
                return i
        i+=1
    return -1