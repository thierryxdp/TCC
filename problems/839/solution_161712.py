def carros(pessoas,capacidade=5):
    automoveis = (pessoas//5)
    modulo = (pessoas%5)
    
    return (automoveis + modulo)