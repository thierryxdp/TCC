def carros(x,y=5):
    """Analisa quantos carros sao necessarios para transportar
    um quantitativo x de passageiros. Visto que cada veiculo
    geralmente possue cinco vagas a não ser se outro modelo, 
    com diferente capacidade(y) for usado; int,int ->float"""
    if x/y==int(x/y):
        return int(x/y)
    else:
        return int(x/y)+1