def pontos_por_time(fase):
    '''Dadas duas listas contendo dois times e o resultado 
    de cada jogo (ida e volta), na ordem em que aparece a 
    pontuação, a função retorna o total de pontos de 
    cada time. lista, lista -> dicionario.'''
    gol_ida_1 = i1
    gol_ida_2 = i2
    gol_volta_1 = v1
    gol_volta_2 = v2
    ida = ['time1','time2',[i1,i2]]
    volta = ['time2','time1',[v1,v2]]
    fase = [ida,volta]
    return {'time1':(i1+v1),'time2':(i2+v2)}