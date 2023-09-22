def carros (pessoas, capacidade=5):
    if pessoas%capacidade!=0:
        result = pessoas // capacidade + 1
    else:
            result = pessoas // capacidade
    return result