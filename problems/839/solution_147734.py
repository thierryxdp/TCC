#Função que retorna o númeor de carros necessários para transportar um numero de pessoas respeitando a lotação de um carro imposta no CTB, após informado numero de pessoasq que vão viajar 
 # int -> int
def carros(pessoas,lugares=5:
    import math
    return math.ceil(pessoas / lugares)