def melhor_volta(matriz):
    '''função que dado uma matriz de 6 corredores com 10 voltas cada um,
    resulta no campeao,na malhor volta e em qual volta'''
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
    return campeao+1, min(melhores_voltas),qual_volta[campeao]+1