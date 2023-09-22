def palavras (frase):
    """recebe uma frase e retorna o numero de palavras nela contidas
    string -> int"""
    
    palavras = str.split(frase)
    
   	return palavras 

    
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
    
    frase = retira_pontuacao(frase)
    return palavras = palavras(frase)