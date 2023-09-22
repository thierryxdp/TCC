def filtraMultiplos(List, N):
    '''Function that filters the numbers of a list and returns
    only the ones that are multiples of a number N, give as 
    parameters the list and the number N, respectively.  
    List, Int --> List.'''
    index = 0
    Multiples = []
    if N == 0:
        if N in List:
            return [N]
        else: 
            return []
    else:
        while index != len(List):
            if List[index]%N == 0:
                Multiples = Multiples + [List[index]]
            index = index + 1 
        return Multiples