# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def alternate_comb(first: list, second: list) -> list:
    assert len(first) == len(second)
 
    n = len(first)
    combined = []
 
    for i in range(n):
        combined.append(first[i])
        combined.append(second[i])
 
    return combined