def faltante(lista):
    ''' uma funcao que ajuda joaozinho a encontrar qual peça está faltando
    do seu quebra cabecas. lista -> int'''
    list.sort(lista)
    contador = 0
    inicio = 1
    list.append(lista, '')
    while inicio == lista[contador]:
        contador += 1
        inicio += 1
    return inicio