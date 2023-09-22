def melhor_volta(matric):
    melho=matric[0][0]
    for i in range(len(matric)):
    	if min(matric[i])<melho:
            melho=min(matric[i])
            corredor=i+1
            qual_volta=matric[i].index(min(matric[i])
	return corredor,melho,qual_volta