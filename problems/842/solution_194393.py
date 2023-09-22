def pontos_por_time (L2):
    """Recebe uma lista dois elementos, ambos listas com o formato ''[time], [time, [gol para cada time]" duas vezes, uma para o jogo de ida e outra pro
    de volta. Então, a função calcula o total de pontos para cada time"""
    lista1 = L2[0]
    lista2 = L2[1]
    
    Ajogo1 = lista1[0]
    Bjogos1 = lista1[1]
    Ajogo2 = lista2[0]
    Bjogo2 = lista2[1]
    
    PontosA = 0
    PontosB = 0
    if Ajogo1>Bjogo1 or Ajogo2>Bjogo2:
        PontosA = PontosA + 3
    if Ajogo1<Bjogo1 or Ajogo2<Bjogo2:
    	PontosB = PontosB + 3
	if Ajogo1 == Bjogo1 or Ajogo2 == Bjogo2:
    	PontosA = PontosA + 3 
        PontosB = PontosB + 3
    return {lista1[0]:PontosA, lista2[0]:PontosB}