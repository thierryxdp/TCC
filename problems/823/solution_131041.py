def faltante(lista):
    """ essa função irá descobrir qual peça esta faltando no tabuleiro de joaozinho
entrada -> lista(int)
saida -> int """
    i=1
    pertence=0
    while i < len(lista):
        if i not in lista:
            pertence = i
        i = i + 1
    return pertence