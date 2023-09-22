def conta_frases (texto):
    string = texto
    characters = "...!?"
    
    string = ''.join( x for x in string if x not in characters)
    
    return string