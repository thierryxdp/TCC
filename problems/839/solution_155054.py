def carros(pessoas,capacidade):
    if (pessoas/capacidade)>1:
        return 1+(pessoas//capacidade)
    else:
        if (pessoas/capacidade)==1:
            return pessoas/capacidade