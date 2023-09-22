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

    
    def inverte(frase):
    """recebe uma frase e retorna a mesma frase, mas com as palavras na ordem
    inversa
    string -> string"""
    
    retira_pontuacao(frase)
    frase.split
    frase.reverse
    frase.join
    
    return frase
    return frase