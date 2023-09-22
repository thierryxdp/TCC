def fatorial(x):
    """ A Função multiplica um numero com o resultado do anterior, assim usando formula do fatorial
    int --> int """
    D = 1
    for n in range(1,x+1):
    	D *= n
	return D