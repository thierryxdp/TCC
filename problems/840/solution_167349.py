def bolos (a:[int], b: [int], c:[int]) -> [int]:
    '''Calcula a quantidade de bolos possíveis de serem feitos seguindo a receita a risca, com os ingredientes à mão'''
    return min ((a//2),(b//3),(c//5))