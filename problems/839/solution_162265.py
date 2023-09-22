def carros(p,l=5):
    """Retorna o numeros de carros necessarios para transportar o numero de pessoas pela quantidade de lugares por carro. Onde p é o número total de passageiros e l a quantidade de lugares em cada carro, sendo 5 o número padrao de vagas. As entradas devem ser números inteiros, pois não existe meia pessoa e o retorno será um número inteiro""" 
    a=(p/l)
    num=ceil(a)
    return num