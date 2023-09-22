def pontos_por_time(ls):
	ret={}
	ida=ls[0]
	vol=ls[1]
	ret={ida[0]:0,ida[1]:0}

	t1=ida[0]
	t2=ida[1]
    
	gt1=ida[2][0]
	gt2=ida[2][1]
	contabilidade(ret,t1,t2,gt1,gt2)

	t1=vol[0]
	t2=vol[1]
	gt1=vol[2][0]
	gt2=vol[2][1]
	contabilidade(ret,t1,t2,gt1,gt2)
    
	return ret

def contabilidade(d,t1,t2,gt1,gt2):
    if gt1<gt2:
    	d[t2]+= 3
    if gt2<gt1:
        d[t1]+= 3
    if gt2==gt1:
        d[t1]+= 1
        d[t2]+= 1