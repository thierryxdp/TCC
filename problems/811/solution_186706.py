def colchao (A,B,C, H,L):
    '''funcao que retorne True se o colchao passa e False se nao passa'''
     A = sorted([int(x) for x in input().strip().split(' ')])
    B = sorted([int(x) for x in input().strip().split(' ')])
     C= sorted([int(x) for x in input().split()])
    

    if A[0] <= B[0] and C[1]:
        return True
    else:
        return False