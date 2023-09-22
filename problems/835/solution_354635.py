def melhor_volta(matric):
    '''recebe como entrada uma matriz 6 x 10 com os tempos em segundos dos corredores em cada volta. A função retorna de quem foi a melhor volta, qual o tempo, e qual a volta; list(list) -> int,int,int'''
    melho=matric[0][0]
    for i in range(len(matric)):
    	if min(matric[i])<melho:
            melho=min(matric[i])
            corredor=i+1
            qual_volta=matric[i].index(min(matric[i])) +1
	return corredor,melho,qual_volta