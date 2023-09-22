def melhor_volta(matriz):
    '''
        Função que, dado o contexto de uma pista de kart que
        permite 10 voltas para cada um dos 6 corredores, recebe
        uma matriz 6x10 com os tempos em segundos dos corredores
        em cada volta (matriz) e retorna uma tupla informando de
        quem foi a melhor volta da prova, com qual tempo e em que
        volta. Todos os corredores tem tempos diferentes. Na matriz,
        cada linha representa uma volta e cada coluna representa um
        corredor;
        list->tuple
    '''
    def melhor_volta(matriz):
    menor_tempo=[]
    volta=[]
    for i in range(len(matriz)):
        menor_tempo+=[min(matriz[i])]
        volta+=[i]
    tupla_tempo=min(menor_tempo)
    tupla_volta=volta[menor_tempo.index(tupla_tempo)]
    tupla_carro=matriz[tupla_volta].index(tupla_tempo)
    return (str(tupla_carro+1)+'° corredor',str(tupla_tempo)+' segundo(s)',str(tupla_volta+1)+'° volta')