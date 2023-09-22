def posLetra(string:str, letra:str, numero:int):
    i=0
    #para saber a ocorrência de determinada letra
    contador = 0
    #Separa todas as palavras como termos de uma lista
    string = string.split()
    #Verifica enquanto I é menor que a string inicial
    while i<len(string):
        #Verifica se a letra é igual na posição I da frase.
        if letra == string[i]:
            contador += 1
        if contador == numero:
            return i
        i+=1 
    return -1