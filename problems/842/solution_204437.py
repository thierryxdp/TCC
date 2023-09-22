def pontos_por_time(tabela):
	""" Função que recebe uma lista com strings da nomes dos times e mais uma lista 
         com o resultado dos jogos. No final, a função retorna um dicionário com a pontu
         a pontuação final da fase.
         lista --> dicionário 
	"""
   	
    
	time1 = tabela[0][0]
	time2 = tabela[0][1]
    pontuacaoTime1 = 0
    pontuacaoTime2 = 0
    
    if tabela[0][2][0] > tabela[0][2][1]:
         pontuacaoTime1 = pontuacaoTime1 + 3
    
    elif tabela[1][2][0] > tabela[1][2][1]:
           pontuacaoTime2 = pontuacaoTime2 + 3
    else:
	    pontuacaoTime1 = pontuacaoTime1 + 1
        pontuacaoTime2 = pontuacaoTime2 + 1
            
    tabelaFinal = {
        time1: pontuacaoTime1,
        time2: pontuacaoTime2}
    
    return tabelaFinal