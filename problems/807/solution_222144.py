def conta_frases(texto):
    """Função que retorna a quantidade de 
    palavras em um texto dado como parâmetro
    str=>int"""
    num_ret = str.count(texto,"...")
    num_pontoF = str.count(texto,".")
    num_pontoEx = str.count(texto,"!")
    num_pontoInt = str.count(texto,"?")
    
    return (num_pontoF - 3*num_ret) + num_pontoEx + num_pontoInt +num_ret