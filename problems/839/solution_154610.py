def carros(a,b=5):
	'''funçao que calcula quantos carros sao necessarios para a viagem;
    int,int->int'''
    
    if a/b - a//b > 0:
        return a//b+1
    else:
        return a//b