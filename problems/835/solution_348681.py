def melhor_volta(seg):
    """Dada uma matriz com os dados de 6 corredores em uma corrida de 10 voltas,
        retorna uma tupla com as informacoes acerca da volta mais rapida
       entrada:
       	seg: lista
       saida: tupla"""

    competidor=0
    mel=[]
    for i in seg:
        for j in i:
            if j==min(i):
                list.append(mel,j)
    best = min(mel)
    for i in seg:
        if best in i:
            return (seg.index(i)+1,best,i.index(best)+1)