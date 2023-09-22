def conta_numero(numero,matriz):
    '''função que dados um número e uma matriz, retorna a quantidade de vezes
       que este número aparece dentro desta matriz. float, list -> int'''
    acum_coluna = 0
    ocorrencia = 0
    for i in matriz:
        acum_linha = 0
        for j in matriz[acum_coluna]:
            if numero == matriz[acum_coluna][acum_linha]:
                ocorrencia += 1
            acum_linha += 1
        acum_coluna += 1
    return ocorrencia