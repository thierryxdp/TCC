def carros(x,y=5):
     if x % y !=0:
        x = math.ceil(x)
    '''funçao que calcula a quantidade de  carros necessarios, sendo x o numero de pessoa e y a capacidade do carro caso seja informada'''
    return x/y