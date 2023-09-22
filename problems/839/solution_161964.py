def carros (pessoas,capacidade=5):
    """int, int -> int"""
    if pessoas>capacidade!=1:
        return round((pessoas/capacidade)+0.5)
    else:
        if pessoas<capacidade:
            return round((pessoas/capacidade)+0.5)
        else:
            if pessoas<=capacidade:
                return int(pessoas/capacidade)
            else:
                if capacidade==1:
                    return pessoas