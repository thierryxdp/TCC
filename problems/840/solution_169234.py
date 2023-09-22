def bolos(A , B , C):
    '''esta funçao calcula a quantidade de bolos que joao pode fazer com os ingretientes que possui'''
    trigo = A/2
    ovos = B/3
    leite = C/5
    return min(trigo, ovos , leite)