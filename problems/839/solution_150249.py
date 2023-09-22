import builtins

def carros(pessoas,capacidade=5):
    ''' Cálculo do número de carros necessários dados uma
    quantidade de pessoas e a capacidade. Se a capacidade
    não for informada, o padrão de 5 será adotado
    int, int -> int '''
    return builtins.ceil(pessoas/capacidade)