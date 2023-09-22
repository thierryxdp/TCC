def faltante(N):
    '''funçao dado uma lista de uma sequencia de numero com um faltando retorna o numero faltante
    list -> int'''
    list.sort(N)
    elemento = 0
    contador = 1
    while contador <= len(N):
        if N[elemento] == contador:
            contador += 1
            elemento += 1
    return contador