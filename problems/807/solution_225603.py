def conta_frases(texto):
    """Função que dado um texto, em string, retorna a 
    quantidade de frases desse texto Entrada -> str; Saída -> int"""
    
    frases = 0
    
    interrogacoes = str.count(texto,"?")
    frases += interrogacoes
    
    exclamacoes = str.count(texto,"!")
    frases += exclamacoes
    
    reticencias = str.count(texto,"...")
    frases += reticencias
    
    pontosfinais = str.count(texto,".")
    pontosfinais -= reticencias*3
    frases += pontosfinais
    
    return frases