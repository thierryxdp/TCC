def pontos_por_time(lista):
    '''
    '''
    jogo1=lista[0]
    jogo2=lista[1]
    result1=jogo1[2]
    result2=jogo2[2]
    pf=0
    pc=0
    #pf=pontos fla#
    #pc=pontos cor#
    
    if result1[0]>result1[1]:
        pc=pc+3
    if result1[0]<result1[1]:
        pf=pf+3
    if result1[0]==result1[1]:
        pf=pf+1
    if result1[0]==result1[1]:
        pc=pc+1
    if result2[0]>result2[1]:
        pf=pf+3
    if result2[0]<result2[1]:
        pc=pc+3
    if result2[0]==result2[1]:
        pf=pf+1
    if result2[0]==result2[1]:
        pc=pc+1

        dicionario={'Flamínthians':pf,
                'Cormengo':pc}
        
        return dicionario