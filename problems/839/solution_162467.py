def carros(pessoas,assentos=5):
    resto= pessoas % assentos
if resto>0:
    return pessoas//assentos + 1
elif resto=0:
    return pessoas//assentos