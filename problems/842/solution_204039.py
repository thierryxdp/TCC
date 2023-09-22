#Start your python function here
def pontos_por_time (lista):
    """retorna um dicionario com o mapeamento <nome do time> -> <numero total de pontos na fase>, para ambos os times"""
    gol_ida1=lista[0][2][0]
    gol_ida2=lista[0][2][1]
    gol_volta2=lista[1][2][0]
    gol_volta1=lista[1][2][1]
    
    if gol_ida1>gol_ida2:
        pontos_ida1=3
        pontos_ida2=0
    elif gol_ida1==gol_ida2:
    	pontos_ida1=1
        pontos_ida2=1
    else:
        pontos_ida1=0
        pontos_ida2=3
        
    if gol_volta1>gol_volta2:
        pontos_volta1=3
        pontos_volta2=0
    elif gol_volta1==gol_volta2:
    	pontos_volta1=1
        pontos_volta2=1
    else:
        pontos_volta1=0
        pontos_volta2=3
        
    return {lista[0][0]:pontos_ida1+pontos_volta1, lista[0][1]:pontos_ida2+pontos_volta2}