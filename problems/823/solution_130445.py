def faltante(x):
    '''retorna a peça de um quebra-cabeças que está faltando;
    list -> int'''
    numero = 1
    y = max([x])
    cont = 0
    while cont < y:
        if numero not in x:
            return numero
        cont = cont + 1
        numero = numero + 1