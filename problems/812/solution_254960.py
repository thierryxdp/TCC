def retira_pontuacao (frase):
    
    """Função que irá remover a pontução de uma frase
    str -> str"""
    
    pontos = ['!', '?',',', '.', '-', ';', ':']
    for trocar in pontos:
        frase = str.replace(frase, trocar, ' ')
    return frase