def melhor_volta(matriztempos):
    '''Retorna uma tupla informando qual corredor fez a melhor volta em uma pista de Kart,
    seu tempo e em qual volta a partir de uma matriz 6x10 em que são contados os tempos de volta
    de 6 corredores, cada um percorrendo 10 voltas
    entrada: list
    saída: tuple
    '''
    temposrecordes=[]
    for corredor in matriztempos:
        list.append(temposrecordes,min(corredor))
    voltarecorde=min(temposrecordes)
    for corredor in matriztempos:
        if voltarecorde in corredor:
            numerovolta=list.index(corredor,voltarecorde)+1
            corredorrecorde= list.index(matriztempos,corredor)+1
            return corredorrecorde, voltarecorde, numerovolta