def pontos_por_time(jogos):
    """define a quantidade de pontos de dois times dados dois jogos.
    entra nome dos times (se tiver time vencedor deve se encontrar na
    primeira posicao) e placar, jogo de ida primeiro e depois o de volta;
    list[list[str,str,list[int,int],list[str,str,list[int,int]]"""
    result1={}
    result2={}
    pontos1={jogos[0][0]:resut1[jogos[0][0]]+result2[jogos[0][0]]
            ,jogos[0][1]:resut1[jogos[0][1]]+result2[jogos[0][1]]}
    pontos2={jogos[0][0]:resut1[jogos[0][0]]+result2[jogos[0][1]]
             ,jogos[0][1]:resut1[jogos[0][1]]+result2[jogos[0][0]]}
    if jogos[0][2][0]>jogos[0][2][1]:
        result1={jogos[0][0]:3,jogos[0][1]:0}
    if jogos[0][2][0]==jogos[0][2][1]:
        result1={jogos[0][0]:1,jogos[0][1]:1}
    if jogos[0][2][0]<jogos[0][2][1]:
        result1={jogos[0][0]:0,jogos[0][1]:3}
    if jogos[1][2][0]>jogos[1][2][1]:
        result2={jogos[1][0]:3,jogos[1][1]:0}
    if jogos[1][2][0]==jogos[1][2][1]:
        result2={jogos[1][0]:1,jogos[1][1]:1}
    if jogos[1][2][0]<jogos[1][2][1]:
        result2={jogos[1][0]:0,jogos[1][1]:3}
    if jogos[0][0]==jogos[1][0]:
        return pontos1
    if jogos[0][0]!=jogos[1][0]:
        return pontos2