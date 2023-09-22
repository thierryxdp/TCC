def hashtag (string):
    ''' função que ao receber uma string, retorna uma nova string semelhante
        com a diferença de que no inìcio, meio e fim da nova string haverá um #
        [str-->str]'''
    
    import math
    if len(string)%2 == 0:
        return '#' + string[: math.ceil ((len(string))/2)] + '#' + string[ math.ceil ((len(string))/2):] + '#'
    else:
        return '#' + string[: (math.ceil ((len(string))/2))-1] + '#' + string[ (math.ceil ((len(string))/2))-1:] + '#'