def conta_frases(texto):
    """Função que conta o número de frases que aparecem em um texto;
       string -> int"""
    texto_sem_espacos = str.strip(texto)
    frases = str.split(texto_sem_espacos,'!')
    frases = [frases[0]] + str.split(frases[1],'?')
    frases = [frases[0],frases[1]] + str.split(frases[2],'...')
    frases = [frases[0],frases[1],frases[2]] + str.split(frases[3],'.')
    return len(frases)