def carros(pessoas, capacidade): 
    if capacidade % pessoas  == 0:
        return capacidade//pessoas
    else:
        return (capacidade//pessoas) + 1