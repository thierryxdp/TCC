def carros(a,b=5):
	'''funçao que calcula quantos carros sao necessarios para a viagem;
    int,int->int'''
    
       y = a / b
       x = a // b

        if (y-x)>0:
            return x + 1
        else:
            return x