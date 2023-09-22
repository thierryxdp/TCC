def contra_frases(frase):
    """Dado como entrada um texto em uma string, a função calcula a
    quantidade de frases nessa string.
    str -> int"""
    
    frases = 0
    
    interrogacoes = str.count(frase,"?")
    frases += interrogacoes
    
    exclamacoes = str.count(frase,"!")
    frases += exclamacoes
    
    reticencias = str.count(frase,"...")
    frases += reticencias
    
    pontosfinais = str.count(frase,".")
    npontosfinais = pontosfinais -= reticencias*3
    
    return frases