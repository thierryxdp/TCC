def faltante(L):
    '''Function that, given a list of number enumerated from
    1 to a specific number N, returns the value of the number
    missing in that interval.
    List --> Int.'''
    list.sort(L)
    index = 0
    value = 1
    while L[index] == value:
        index = index + 1
        value = value + 1 
    return value