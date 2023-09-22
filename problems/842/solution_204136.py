def pontos_por_time(lista0):
    """Função que retorna um dicionário com o time e seu total de pontos< list,list ->dicionário."""
    jogo1=lista0[0]
    jogo2=lista0[1]
    gols1= jogo1[2]
    carmengo1=gols1[0]
    flaminthians1=gols1[1]
    gols2=jogo2[2]
    carmengo2=gols2[1]
    flaminthians2=gols2[0]
    if carmengo1==flaminthians1==0 and carmengo2==flaminthians2==0:
        tabela = {'Carmengo': '2 pontos', 'Flaminthians': '2 pontos'}
        return tabela
    if carmengo1==flaminthians1==0 and carmengo2>flaminthians2:
        tabela = {'Carmengo': '4 pontos', 'Flaminthians': '1 ponto'}
        return tabela
    if carmengo1==flaminthians==0 and carmengo2<flaminthians2:
        tabela = {'Carmengo': '1 ponto', 'Flaminthians': '4 pontos'}
        return tabela
    if carmengo1>flaminthians1 and carmengo2==flaminthians2==0:
        tabela = {'Carmengo': '4 pontos', 'Flaminthians': '1 ponto'}
        return tabela
    if carmengo1<flaminthians1 and carmengo2==flaminthians2==0:
        tabela = {'Carmengo': '1 pontos', 'Flaminthians': '4 ponto'}
        return tabela
    if carmengo1>flaminthians1 and carmengo2>flaminthians2:
        tabela = {'Carmengo': '6 pontos', 'Flaminthians': '0 pontos'}
        return tabela
    if  carmengo1>flaminthians1 and carmengo2<flaminthians2:
        tabela = {'Carmengo': '3 pontos', 'Flaminthians': '3 pontos'}
        return tabela
    if carmengo1<flaminthians1 and carmengo2>flaminthians2:
        tabela = {'Carmengo': '3 pontos', 'Flaminthians': '3 pontos'}
        return tabela
    if carmengo1>flaminthians1 and carmengo2>flaminthians2:
        tabela = {'Carmengo': '0 pontos', 'Flaminthians': '1 pontos'}
        return tabela