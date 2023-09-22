def posLetra(string, letra, numero):
    i=0
    #para saber a ocorrência de determinada letra
    contador = 0
    #Verifica enquanto I é menor que a string inicial
    while i<len(string):
        #Verifica se a letra é igual na posição I da frase.
        if letra == string[i]:
            contador += 1
        if contador == numero:
            return i
        i+=1 
    return -1