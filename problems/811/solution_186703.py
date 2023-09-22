def colchao (A,B,C, H,L):
    '''funcao que retorne True se o colchao passa e False se nao passa'''
     mattress_dimen = sorted([int(x) for x in input().strip().split(' ')])
    door_dimen = sorted([int(x) for x in input().strip().split(' ')])
    mattress_dimen = sorted([int(x) for x in input().split()])
    door_dimen = sorted([int(x) for x in input().split()])

    if mattress_dimen[0] <= door_dimen[0] and mattress_dimen[1] <= door_dimen[1]:
        return True
    else:
        return False