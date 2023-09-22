def pontos_por_time(ls)
	ida=ls[0] #[['Cormengo','Flamínthians',[,]]
	vol=ls[1]
	ret={ida[0]:0,ida[1]:0}

	t1=ida[0]
	t2=ida[1]
	gt1=ida[2][0]
	gt2=ida[2][1]

	contabilidade(ret,t1,t2,gt1,gt2)

	t1=ida[0]
	t2=ida[1]
	gt1=ida[3][0]
	gt2=ida[3][1]

	contabilidade(ret,t1,t2,gt1,gt2)
	return ret

def contabilidade(ret,t1,t2,gt1,gt2):
    if gt1<gt2:
    	ret[t2]+=3
    if gt2<gt1:
        ret[t1]+=3
    if gt2==gt1:
        ret[t1]+=1
        ret[t2]+=1