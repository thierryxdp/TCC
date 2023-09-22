def melhor_volta(matriz):
        """Função que recebe como entrada uma matriz 6 x 10 com os tempos em
        segundos dos corredores em cada volta. A função deve retornar uma
        tupla informando: De quem foi a melhor volta da prova,
        com qual tempo e em que volta.
        list(list) -> tupla(int, int,int)
        """
        local_menor_volta = min(matriz)
        corredor = matriz.index(local_menor_volta)+1
        tempo = min(matriz[matriz.index(local_menor_volta)])
        num_volta = matriz[matriz.index(local_menor_volta)].index(tempo)+1
        return (corredor,tempo,num_volta)