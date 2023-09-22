def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    texto_sem_espacos = str.strip(texto)
    if '!' in texto_sem_espacos:
        frases = str.split(texto_sem_espacos,'!')
        num_frases1 = len(frases) - 1
    if '?' in texto_sem_espacos:    
        frases = str.split(texto_sem_espacos,'?')
        num_frases2 = len(frases) - 1
    if '...' in texto_sem_espacos:
        frases = str.split(texto_sem_espacos,'...')
        num_frases3 = len(frases) - 1
    if '.' in texto_sem_espacos:
        frases = str.split(texto_sem_espacos,'.')
        num_frases4 = len(frases) - 1
    return num_frases1 + num_frases2 + num_frases3 + num_frases4