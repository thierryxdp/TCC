def posLetra(string, letra, numero):
    '''Recebe uma string, uma letra e um número(ocorrência 
    desejada da letra) e retorna a posição da stirng aquela
    ocorrência da letra. Caso as ocorrências da letra sejam 
    menores que as pedidas, a função retorna -1'''
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