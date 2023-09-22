def eh_quadrada(matrizQuad):
        # Função que dada uma matriz, verifica se ela é quadrada
        # list -> bool
    for i in range(0, len(matrizQuad)):
        for counter in range(0, len(matrizQuad[i])):
            if len(matrizQuad) == len(matrizQuad[i]) and len(matrizQuad[counter]):
                return True
            else:
                return False
    return True