def faltante(lista):
    """ essa função irá descobrir qual peça esta faltando no tabuleiro de joaozinho
entrada -> lista(int)
saida -> int """
    i=1
    pertence=0
    while i in lista:
        i = i + 1
    return i