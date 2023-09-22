#Exercício 2 - Quantos carros são necessários?
def carros(p, c = 5):
    'int, int -> int'
    '''Essa função recebe a quantidade de pessoas a serem transportadas (p)
        e a capacidade do carro (c), respectivamente. Caso a capacidade não
        seja informada, a capacidade assume o valor padrão de 5 lugares. A
        função retorna o número de carros necessários para o transporte,
        usando o a função ceil do módulo math para arredondar para cima, caso
        sobrem vagas. Nenhum dos argumentos pode receber valores negativos, se
        receberem a função não funcionará corretamente.'''
    return ceil(p/c)