def pontos_por_time(X):
    '''receba uma lista de dois elementos, onde cada elemento é também uma lista. A lista completa tem informações do número de gols em dois jogos de futebol entre dois times (jogo da ida e jogo da volta)
    list->dicionario'''
    jogolda=X[0]
	placarida=jogolda[2]
    time1=jogolda[0]
    placarVolta=jogoVolta[2]
	time2=jogolda[1]
    jogoVolta=X[1]
    
	if placarida[0]==placarida[1]:
        pjogoida=1,1
	if placarida[0]>placarida[1]:
        pjogoida=3,0 
    if placarida[0]<placarida[1]:
		pjogoida=0,3 
    if placarVolta[0]==placarVolta[1]:
		pjogovolta=1,1 
    if placarVolta[0]>placarVolta[1]:
        pjogovolta=3,0
	if placarVolta[0]<placarVolta[1]:
		pjogovolta=0,3
        
	ptime1= pjogoida[0]+pjogovolta[1]
	ptime2= pjogoida[1]+pjogovolta[0]

	return (time1:ptime1,time2:ptime2]