def faltante(lista):
    if lista:
        inteito=lista[0]
        posicao=1
        while posicao<len(lista):
            if (inteiro+1) < lista[posicao]:
                inteiro=inteiro+1
                yield inteiro
            else:
                inteiro=lista[posicao]
                posicao=posicao+1