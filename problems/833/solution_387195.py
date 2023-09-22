def conta_numero(numero,matriz):
    '''essa função recebe uma matriz e retorna somente o nome daqueles que são de determinado setor'''
    '''str, list -> list'''
    numero = str.lower(numero)
    funcionarios_encontrados = []

    for i in range(len(matriz)) :
     if numero in str.lower(matriz[i][2]):
        cargo = matriz[i]
        del cargo[2]
        funcionarios_encontrados.append(cargo)
    return funcionarios_encontrados