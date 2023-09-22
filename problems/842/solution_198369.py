def pontos_por_time(lista):
	len(lista)==2
	gols_a_ida=lista[0][2][0]
	gols_b_ida=lista[0][2][1]
	gols_a_volta=lista[1][2][1]
	gols_b_volta=lista[1][2][0]
	pontuacao_ida_time_a=[]
	pontuacao_ida_time_b=[]
	if gols_a_ida>gols_b_ida:
		pontuacao_ida_time_a=pontuacao_ida_time_a.append(3)
	if gols_b_ida>gols_a_ida:
		pontuacao_ida_time_b=pontuacao_ida_time_b.append(3)
	if gols_a_ida==gols_b_ida:
		pontuacao_ida_time_a=pontuacao_ida_time_a.append(0)
	if gols_b_ida==gols_a_ida:
		pontuacao_ida_time_b=pontuacao_ida_time_b.append(0)
	pontuacao_volta_time_a=[]
	pontuacao_volta_time_b=[]
	if gols_a_volta>gols_b_volta:
		pontuacao_volta_time_a=pontuacao_volta_time_a.append(3)
	if gols_b_volta>gols_a_volta:
		pontuacao_volta_time_b=[]
	if gols_a_volta==gols_b_volta:
		pontuacao_volta_time_a=pontuacao_volta_time_a.append(0)
	if gols_b_volta==gols_a_volta:
		pontuacao_volta_time_b=pontuacao_volta_time_b.append(0)
	pontuacao_total_time_a=pontuacao_ida_time_a[0]+pontuacao_volta_time_a[0]
	pontuacao_total_time_b=pontuacao_ida_time_b[0]+pontuacao_volta_time_b[0]
	time
	dic ={lista[0][0]:pontuacao_total_time_a,lista[1][0]:pontuacao_total_time_b}
	return dic