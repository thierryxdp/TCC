def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    texto_sem_espacos = str.strip(texto)
    if '!' in texto:
        frases = str.split(texto_sem_espacos,'!')
    if '?' in texto: 
        frases = str.split(texto_sem_espacos,'?')
    if '...' in texto:
        frases = str.split(texto_sem_espacos,'...')
    if '.' in texto: 
        frases = str.split(texto_sem_espacos,'.')
    return len(frases)