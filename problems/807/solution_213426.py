def conta_frases(text):
    """
    
    """
	var = str.count(text,'.') + str.count(text,'?') + str.count(text,'!') - 2 * str.count(text,'...')
    
    return  var