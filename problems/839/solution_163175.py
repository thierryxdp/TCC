def carros(pessoas,capacidade=5):

    automoveis = pessoas//capacidade
    x = ((pessoas/capacidade) - automoveis)*capacidade

    return(x + automoveis)