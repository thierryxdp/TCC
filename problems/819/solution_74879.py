def filtraMultiplos (lista, divisor):
    ''' função que filtra de dentro de uma lista inicial de números
        apenas os que sejam divisíveis pelo número fornecido(divisor),
        retornando uma nova lista com esses números 
        [list,int-->list]'''

    novalista = []
    indice = 0

    while indice < len(lista):
        
        if lista[indice] % divisor == 0 :
            novalista += [lista[indice]]
            
        indice += 1

    return novalista