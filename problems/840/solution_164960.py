def bolos (a, b, c):
    """Calcula quantos bolos podem ser feitos de acordo com uma receita que requer as seguintes proporções de ingredientes: 2 xícaras de farinha (f), 3 ovos (o), 5 colheres de sopa de leite (l). float, int (ovo), float -> int"""
    return int(min (a/2, b/3, c/5))