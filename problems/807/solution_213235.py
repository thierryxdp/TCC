def conta_frases (texto):
    """Função que calcula o número de frases que o texto de entrada possui, sendo separadas por '.', '...', '?' ou '!'
    entrada: string
    saída: int"""
    
    return len(str.split(texto, '.','...'))