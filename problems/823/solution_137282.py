def faltante(pecas):
    """A função recebe como entrada uma lista em ordem crescente
    ou decrescente de números correspondentes às peças de 
    um quebra-cabeças e retorna um inteiro que representa
    a peça faltante."""
    if pecas[0] < pecas[-1]:
        i = 1
        while i < len(pecas):
            if pecas[i] - pecas[i-1] != 1:
                return pecas[i-1] + 1
            else:
                i+=1
        return pecas[i-1] + 1
        
    if pecas[0] > pecas[-1]:
        i = 0
        while i < len(pecas):
            if pecas[i] - pecas[i+1] != 1:
                return pecas[i] - 1
            else:
                i+=1
        return pecas[i] - 1