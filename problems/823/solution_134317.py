def faltante(lista):
    '''Funcao recebe uma lista com numeros de um quebra cabeca numerado de 1 a N e retorna o valor de n que esta faltandon
list -> int'''
    contador = 0
    valor = 1
    faltando = 0
    while (lista[contador] == valor):
        valor +=1
        contador += 1
    return valor