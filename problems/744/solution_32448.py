def hashtag(s):
    ''' Essa função concatena uma string colocando # no começo,
    no meio e no final do texto
    string -> string'''
    
    meio = len(s)/2
    
    return '#'+ s[:int(meio)] +'#'+ s[int(meio):] +'#'