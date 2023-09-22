def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    texto_sem_espacos = str.strip(texto)
    numero_frases = str.count(texto_sem_espacos,'!')+ str.count(texto_sem_espacos,'?')+ texto_sem_espacos,'...')+ texto_sem_espacos,'. ')
    return numero_frases