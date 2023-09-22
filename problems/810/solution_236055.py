def retira_pontuacao(frase):
    """Recebe uma frase e retorna uma nova onde todas as pontuações estão
    trocadas por espaços"""
    frase = frase.lower()
    nova_frase = frase.replace('.', ' ')
    nova_frase = nova_frase.replace('!', ' ')
    nova_frase = nova_frase.replace('?', ' ')
    nova_frase = nova_frase.replace(',', ' ')
    nova_frase = nova_frase.replace('-', ' ')
    nova_frase = nova_frase.replace(':', ' ')
    nova_frase = nova_frase.replace('...', ' ')
    nova_frase = nova_frase.replace('  ', ' ')
    nova_frase = nova_frase.replace(';', ' ')
    return nova_frase

def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    nova_frase = frase.lower()
    nova_frase1 = retira_pontuacao(nova_frase)
    nova_frase = nova_frase1.split()
    nova_frase = nova_frase[-1::-1]
    nova_frase = str.join(' ', nova_frase)
    return nova_frase