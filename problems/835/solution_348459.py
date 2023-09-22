def melhor_volta(mt):
    '''Função que retorna uma tupla informando: De quem 
    foi a melhor da prova, com qual tempo e em que volta.
    mt=list->tuple'''
    tf=[]
    for p in range(len(mt)):
        for w in range(len(mt[p])):
            mn=min(mt[p])
            tf.append(mn)
            rs=min(tf)
            if mt[p][w]==rs:
                ps=p+1
                vt=w+1
    return vt,rs,ps