def pontos_por_time(listajogo1,listajogo2):
	"""Define os pontos de cada time apos jogo de ida e volta.
Lista->lista"""
	#ida#
	time1=listajogo1[0]
	time2=listajogo1[1]
	result=(listajogo1[2])
	#volta#
	time2=listajogo2[0]
	time1=listajogo2[1]
	result1=(listajogo2[2])
	#
	res1=result[0]
	res2=result[1]
	res3=result1[1]
	res4=result1[0]
	#
	resp1=()
	resp0=()
	#
	if res1>res2:
		resp0+=(3,)
		resp1+=(0,)
	if res1==res2:
		resp0+=(1,)
		resp1+=(1,)
	if res4>res3:
		resp0+=(3,)
		resp1+=(0,)
	#
	if res2>res1:
		resp1+=(3,)
		resp0+=(0,)
	if res3>res4:
		resp0+=(3,)
		resp1+=(0,)
	if res3==res4:
		resp0+=(1,)
		resp1+=(1,)
	return str(time1 )+str(resp0[0]+resp0[1])+str(' pontos e ')+str(time2 )+str(resp1[0]+resp1[1])+str(' pontos .')#Start your python function here