def conta_frases(text):
    """
    
    """
    Str.count(text,'.') + str.count(text,'?') + str.count(text,'!') - 2 * str.count(text,'...')