def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos inteiros, e retorna
    uma nova tupla contendo apenas os elementos pares da original,
    na mesma ordem em que se encontravam.
    tuple -> tuple'''
    #Criamos uma tupla vazia para a resposta
    final = ()
     #Verificamos se o valor em cada posição é par, e caso seja,
     #concatenamos a tupla unitária composta por ele com a nossa vazia.
     #Fazemos isso para todas os valores da tupla recebida.
    if tupla[0] % 2 == 0:
        final += (tupla[0],)  
    if tupla[1] % 2 == 0:
        final += (tupla[1],)
    if tupla[2] % 2 == 0:
        final += (tupla[2],)
    if tupla[3] % 2 == 0:
        final += (tupla[3],)
     #Agora, basta retornar a tupla que concatenamos.
    return final