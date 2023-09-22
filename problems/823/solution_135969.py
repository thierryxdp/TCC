def faltante(lista):
    ''' retorna o número faltando em uma sequencia de inteiros de 1 a N, para assim
    determinar que peça falta no tabuleiro;
    list -> int '''
    i=1
    while i < N:
        if lista[i]-lista[i-1]>1:
            return i-1
        i=i+1