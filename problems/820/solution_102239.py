def posLetra(string,letra,ocorrencia):
    """função que retorna a posição da letra na ocorrencia desejada
    str,str,int->int"""
    if str.count(string,letra)>=ocorrencia:
		beg=0
    	ocorr=1
    	while ocorr<ocorrencia:
        	beg=str.find(string,letra,beg+1)
        	ocorr=ocorr+1
        return str.find(string,letra,beg)    
    else:
        return -1