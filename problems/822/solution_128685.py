repetidos(List):
    '''Function that, given a List of numbers as parameter,
    returns the quantity of times that a number is equal to 
    one right behind it.
    List --> Int'''
    index = 0
    repetitions = 0
    while index != len(List)-1:
        if List[index] == List[index + 1]:
            repetitions = repetitions + 1
        index = index + 1  
    return repetitions