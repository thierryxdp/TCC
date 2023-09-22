def num_bombons(a,b):
    '''a é o dinheiro e b o valor do bombom'''
    return max(a,b), num_bombons(a/b)