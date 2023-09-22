def pontos_por_time(fase):
    '''Dadas duas listas contendo dois times e o resultado 
    de cada jogo (ida e volta), na ordem em que aparece a 
    pontuação, a função retorna o total de pontos de 
    cada time. lista, lista -> dicionario.'''
    ida = ['time1','time2',gol_ida1,gol_ida2]
    volta = ['time2','time1',gol_volta2,gol_volta1]
    fase = [[ida],[volta]]
    return {'time1':(gol_ida1+gol_volta1),'time2':(gol_ida2+gol_volta2)}