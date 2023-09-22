def retira_pontuacao(frase):
    """recebe uma frase e substitui todas as pontuacoes por espacoes em branco
    string -> string"""
    
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '...', ' ')
    
    return frase

    
def inverte(frase):
    """recebe uma frase e retorna a mesma frase, mas com as palavras na ordem
    inversa
    string -> string"""
    
    frase = retira_pontuacao(frase)
    
    palavras = frase.split()
    
    invertida = ' '.join(reversed(palavras))
    
    return str.lower(invertida)