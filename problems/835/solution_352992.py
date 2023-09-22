def melhor_volta(matriz):

    menores_tempos = []

    volta_dos_menores_tempos = []

    for matrizes in matriz:

        menores_tempos.append(min(matrizes))

        volta_dos_menores_tempos.append(matrizes.index(min(matrizes)))

    de_quem_foi = menores_tempos.index(min(menores_tempos))+1

    qual_tempo = min(menores_tempos)

    qual_volta = matriz[de_quem_foi-1].index(min(matriz[de_quem_foi]))

    return (de_quem_foi, qual_tempo, qual_volta)