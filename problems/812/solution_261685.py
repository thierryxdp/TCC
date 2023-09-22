def retira_pontuacao(frase):
    """recebe uma frase e substitui todas as pontuacoes por espacoes em branco
    string -> string"""
    
    str.replace(frase, '.', ' ')
    str.replace(frase, ',', ' ')
    str.replace(frase, '-', ' ')
    str.replace(frase, ';', ' ')
    str.replace(frase, ':', ' ')
    str.replace(frase, '!', ' ')
    str.replace(frase, '?', ' ')
    str.replace(frase, '...', ' ')
    
    return frase