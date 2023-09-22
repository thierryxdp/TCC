def retira_pontuacao(frase):
    """Recebe uma frase e retorna uma nova onde todas as pontuações estão
    trocadas por espaços"""
    frase = frase.lower()
    frase = frase.replace('.', ' ')
    frase = frase.replace('!', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace(',', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('...', ' ')
    frase = frase.replace('  ', ' ')
    frase = frase.replace(';', ' ')
    return frase

def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    frase = retira_pontuacao(frase)
    frase = frase.split()
    frase = frase[-1::-1]
    frase = str.join(' ', frase)
    return frase