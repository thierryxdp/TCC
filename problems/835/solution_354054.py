def melhor_volta(matriz):
    'Função que recebe uma matriz de tempos de voltas em segundos de uma corrida e retorna quem fez a melhor volta, quanto ela vale e em qual volta ela foi exercida.'
    'list->tuple'

    lista=[]
    x=len(matriz[0])
    y=len(matriz)
    c=0

    for corredor in matriz:
        for volta in corredor:
            lista=lista+[volta]

    m_tempo=min(lista)

    while c!=y:
        if m_tempo in lista[(x*c):(x*c)+(x)]:
            m_piloto=c+1
            lista_n=lista[(x*c):(x*c)+(x)]            
        c=c+1

    n_volta=list.index(lista_n,m_tempo)+1   
        
    return (m_piloto, m_tempo, n_volta)