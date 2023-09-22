from random import randint
def dois_dados():
    """Dados dois dados, conta quantas vezes os dados foram
    jogados ate que saiam numeros repetidos."""
    n = 1
    rand1 = randint(1,6)
    rand2 = randint(1,6)
    while rand1 != rand2:
        n += 1
        rand1 = randint(1,6)
        rand2 = randint(1,6)
    return n