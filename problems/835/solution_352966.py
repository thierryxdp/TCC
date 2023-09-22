def melhor_volta(matriz):

    menores_tempos = []

    volta_dos_menores_tempos = []

    for matrizes in matriz:

        menores_tempos.append(min(matrizes))

        volta_dos_menores_tempos.append(volta_dos_menores_tempos.index(min(matrizes)))

    return (menores_tempos.index(min(menores_tempos)+1), min(menores_tempos), volta_dos_menores_tempos.index(min(volta_dos_menores_tempos)))