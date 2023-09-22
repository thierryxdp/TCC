def bolos(A: int, B: int, C: int) -> int:
    '''Calcula e retorna o número de bolos possíveis para
    serem criados a partir de uma medida A de xícaras de
    farinha de trigo, B de ovos e C de colheres de sopa de
    leite, tendo em vista a produção de bolos inteiros
    com medidas padrão de ingredientes'''
    return min(A/2 + B/3 + C/5)