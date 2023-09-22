def posLetra(String, Letter, Occurrence=1):
    '''Function that given a string, a letter and a number
    for the occurrence (First, seconde, third...), 
    respectively, returns the position that the given occurrence
    of the letter occupies in the string.
    Str, Str, Int --> Int.'''
    NumbOfOcurrences = str.count(String, Letter)
    OccurrencesCounter = 0
    Interval = 0 #Analises the string from the position 'Interval' and beyond.
    if NumbOfOcurrences < Occurrence:
        return -1
    else:
        while OccurrencesCounter != Occurrence:
        	Position = str.find(String, Letter, Interval)
            OccurrencesCounter = OccurrencesCounter + 1 
            Interval = Position + 1 
    return Position