def pontos_por_time(lista):
    'Função que retorna pontuação dos times.'
    'list -> list'
    return sum(lista[0][2]) + sum(lista[1][2]) + sum(lista[2][2])