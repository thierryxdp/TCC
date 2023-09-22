def retira_pontuacao (frase):
    
    """Função que irá remover a pontução de uma frase
    str -> str"""
    
    pontos = ['!', '?',',', '.', '-', ';', ':']
    for trocar in pontos:
        frase = frase.replace(trocar, ' ')
    return frase

def inverte (frase):
    """Função que ao receber uma frase inverte a ordem das 
    palavras, remove as letras maiusculas e remove a pontuação
    str -> str"""
    
    pontos = retira_pontuacao (frase)
    retira_maiusculas = pontos.lower ()
    retira_espaco = retira_maiusculas.strip ()
    frase_split = retira_espaco.split () [::-1]
    frase_join = " ".join (frase_split)
    
    return frase_join