def filtraMultiplos(lista,n):
    '''Função feita para filtrar os múltilos de um número(n), recebendo o próprio número e uma lista como entrada.Retorna outra lista contendo os elementos da lista de entrada, que forem múltilos do número 'n'.
       parâmetros de entrada:list, int
       valor de retorno:list'''
    multiplos=[]
    contador=0
    while contador<len(lista):
        if lista[contador]%n==0:
            multiplos=multiplos+[lista[contador]]
        contador=contador+1
    return multiplos