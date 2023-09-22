def par(numero):
    '''Funcao booleana que retorna true quando passamos um numero par.
        Parametro de Entrada: int
        Valor de retorno: bool'''
    return numero%2 == 0

def filtra_pares(tupla):
    '''recebe tupla com 4 numeros inteiros e retorna outra tupla com somente os numeros pares
    entrada: int; saida: tupla'''
    lista_pares = filter(par, tupla)
    print lista_pares