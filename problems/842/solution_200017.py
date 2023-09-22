def pontos_por_time([timeA,timeB,golsA1,golsB1][timeB,timeA,golsB2,golsA2]):
    '''funcao que calcula quais dos times,timeA(Cormengo),timeB(Flaminthias) se saiu vitoriosa apos dois jogos disputados contra
    list,list->dicionario'''
    (Ponto_Cormengo1=(golsA1>golsB1))=3 + (Ponto_Cormengo2=(golsA2>golsB2))=3
    (Ponto_Flaminthians1=(golsB1>golsA1))=3 + (Ponto_Flaminthians2=(golsB2>golsA2))=3
    (Empate=(golsB1=golsA1))=1 or + (Empate=(golsB2=golsA2))=1 
    Saldo_gols_A=(golsA1+golsA2)
    Saldo_gols_B=(golsB1+golsB2)
    if (Ponto_Cormengo1>Ponto_Flaminthians1) and (Ponto_Cormengo2>Ponto_Flaminthians2):
        return 'Cormengo' and Saldo_golsA