def bolos(a,b,c):
    '''funçao q recebe a quantidade dos ingredientes de um bolo e 
    	retorna a quantidade de bolos q sao possiveis de ser feitos
        int/float ->int
        questao 3'''
    if(a//2)<=(b//3) and (a//2)<=(c//5):
    	return a//2 
    elif (b//3)<=(a//2) and (b//3)<=(c//5):
        return b//3
    elif (c//5)<=(a//2) and (c//5)<=(b//3):
        return c//5