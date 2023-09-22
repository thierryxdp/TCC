def faltante(lista):
    '''Descobre qual o número da peça do quebra-cabeça de Joãzinho
    que está faltando.
    lista -> int'''                    
    indice = 0
    numero = 1
    faltou= 0
    while indice <= len(lista):
        if numero not in lista:
            faltou = numero
        indice += 1
        numero+= 1
    return faltou