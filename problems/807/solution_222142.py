def conta_frases(texto):
    num_ret = str.count(texto,"...")
    num_pontoF = str.count(texto,".")
    num_pontoEx = str.count(texto,"!")
    num_pontoInt = str.count(texto,"?")
    
    return num_pontoF + num_pontoEx + num_pontoInt + num_ret