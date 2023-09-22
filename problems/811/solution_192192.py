def colchao(medidas,H,L):
    ''' função que calcula e responde se um colchao dadas suas medidas,
    passa em uma porta( dadas suas medidas H e L), sendo que ele será
    passado com uma das faces paralelas ao chao'''
    '''list,int,int->bool'''
    if(medidas[1]<= H)or(medidas[2]<=L):
    	return True
    else:
        return False