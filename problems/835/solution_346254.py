def melhor_volta(matriz):
        """Função que recebe como entrada uma matriz 6 x 10 com os tempos em
        segundos dos corredores em cada volta. A função deve retornar uma
        tupla informando: De quem foi a melhor volta da prova,
        com qual tempo e em que volta.
        list(list) -> tupla(int, int,int)
        """
        melhores_voltas =[]
        for i in range(len(matriz)):
                melhores_voltas.append(min(matriz[i]))
        melhor_todas = min(melhores_voltas)
        corredor = list.index(melhores_voltas,melhor_todas) + 1
        num_volta = list.index(matriz[corredor-1],melhor_todas)+1
        return (corredor,melhor_todas,num_volta)