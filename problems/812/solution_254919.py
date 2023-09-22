def retira_pontuacao (frases):
    
    """Função que irá remover a pontução de uma frase
    str -> str"""
    
    pontos = ['!', '?',',', '.', '-', ';', ':']
    for trocar in pontos:
        frase = frases.replace(trocar, '')
    return frase