def bolos(trigo,ovo,colher):
    '''retorna a quantidade mínima de bolos possíveis de serem feitos dados as quantidades de farinha de trigo, ovos e colhres de sopa de leite'''
    trigo = trigo // 2
    ovo = ovo // 3
    colher = colher // 5
    return min(trigo,ovo,colher)