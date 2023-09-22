def pontos_por_time(jogos):
	"""retorna a tabela de pontos dados dois confrontos entre times.
entra nome dos times sendo o sediador o primeiro e depois o placar;
list[list[str,str,list[int,int]],list[str,str,list[int,int]]]->dict{str:int,str:int}"""
	jogos[0][0]==jogos[1][1]
	jogos[0][1]==jogos[1][0]
	if jogos[0][2][0]>jogos[0][2][1]:
		result1={jogos[0][0]:3,jogos[0][1]:0}
	if jogos[0][2][0]<jogos[0][2][1]:
		result1={jogos[0][0]:0,jogos[0][1]:3}
	if jogos[0][2][0]==jogos[0][2][1]:
		result1={jogos[0][0]:1,jogos[0][1]:1}
	if jogos[1][2][0]>jogos[1][2][1]:
		result2={jogos[1][0]:3,jogos[1][1]:0}
	if jogos[1][2][0]<jogos[1][2][1]:
		result2={jogos[1][0]:0,jogos[1][1]:3}
	if jogos[1][2][0]==jogos[1][2][1]:
		result2={jogos[1][0]:1,jogos[1][1]:1}
	pontos={jogos[0][1]:result1[jogos[0][1]]+result2[jogos[0][1]],jogos[0][0]:result1[jogos[0][0]]+result2[jogos[0][0]]}
    return pontos