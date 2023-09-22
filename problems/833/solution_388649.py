def conta_numero(numero,matriz):
    '''Function that given a interger and a matrix of
    intergers, respectively, as parameters, returns the
    number of times that number appears inside the matrix.
    Int, List --> Int.'''
    Occurrences = 0
    for line in matriz:
        for number in line:
            if number == numero:
                Occurrences += 1
    return Occurrences