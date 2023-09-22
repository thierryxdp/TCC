def carros(pessoas,capacidade=5):

    automoveis = pessoas//capacidade
    x = ((pessoas/capacidade) - automoveis)
    if x=0:
        return(automoveis)
    if x>0:
        return(1 + automoveis)