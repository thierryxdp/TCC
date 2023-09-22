def carros (pessoas,capacidade=5):
    """int, int -> int"""
    if pessoas>capacidade:
        return round((pessoas/capacidade)+0.5)
    elif pessoas<=capacidade:
        return (pessoas/capacidade)
    else: