def carros(num_pass,cap_carro=5):
    """ Função que define a quantidade de carros necessarrios para transportar tantas pessoas."""
    qnt_carros=num_pass/cap_carro
    Num_carros=math.ceil(qnt_carros/cap_carros)

         return int(Num_carros)