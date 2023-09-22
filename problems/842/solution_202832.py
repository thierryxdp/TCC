def pontos_por_time(fase):
    '''Dadas duas listas contendo dois times e o resultado 
    de cada jogo (ida e volta), na ordem em que aparece a 
    pontuação, a função retorna o total de pontos de 
    cada time. lista, lista -> dicionario.'''
    ida = ['time1','time2',gol_ida_1,gol_ida_2]
    volta = ['time2','time1',gol_volta_2,gol_volta_1]
    fase = [[ida],[volta]]
    return {'time1':(gol_ida_1+gol_volta_1),'time2':(gol_ida_2+gol_volta_2)}