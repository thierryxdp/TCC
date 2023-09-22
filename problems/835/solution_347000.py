def melhor_volta(matriz):

    """ Organizemos as informações sobre 6 corredores durante 10 voltas numa
        corrida de kart numa matriz. Obtendo estas informações, queremos saber
        o corredor que percorreu a volta mais rápida, quanto foi este valor
        e em qual volta isto foi feito. Os corredores vão de 1 até 6, as voltas
        vão de 1 até 10. As informações de saída numa tupla estão nesta repectiva
        ordem: Qual corredor que obteve o menor tempo, o menor tempo, e em qual
        volta foi feito o menor tempo.
        list -> tuple
    """

    tempo_voltas = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tempo_voltas = tempo_voltas + [matriz[i][j]]
            
    menor_tempo = min(tempo_voltas)
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (matriz[i][j] == menor_tempo):
                resultado = (i+1,menor_tempo,j+1)
                
    return resultado