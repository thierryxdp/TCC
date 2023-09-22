def melhor_volta(matriz):
    ''''''retorna o campeao de uma corrida, sua melhor volta e o tempo da volta
    matriz -> tupla''''''
    resultado = ()
    melhores_voltas = []
    qual_volta = []
    for corredor in matriz:
        lista_voltas = []
        for voltas in corredor:
            list.append(lista_voltas, voltas)
        list.append(melhores_voltas, min(lista_voltas))
        list.append(qual_volta, list.index(lista_voltas,(min(lista_voltas))))
        campeao = list.index(melhores_voltas,min(melhores_voltas))
    return campeao+1, min(melhores_voltas),qual_volta[campeao+1]