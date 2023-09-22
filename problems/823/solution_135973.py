def faltante(lista):
    ''' retorna o número faltando em uma sequencia de inteiros de 1 a N, para assim
    determinar que peça falta no tabuleiro;
    list -> int '''
    i=0
    while i < len(lista)- 1:
        if lista[i]!=i+1:
            return i+1 
        i=i+1