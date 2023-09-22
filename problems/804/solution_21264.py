def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros
    e retorna uma nova tupla"""
    pares = []
    for elemento in tupla:
        if elemento %2==0:
            pares.append(elemento)
            return tupla(pares)