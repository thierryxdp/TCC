def carros(pessoas=0,capacidade=5):
    "calcula o numero de carros necessarios p certo numero de pessoas,dada a sua capacidade"
    return sum(round(pessoas/capacidade))