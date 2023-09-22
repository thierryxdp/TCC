def retira_pontuacao(frase):
    """Recebe uma frase e retorna uma nova onde todas as pontuações estão
    trocadas por espaços"""
    frase_nova = frase.replace('.', ' ')
    frase_nova = frase_nova.replace('!', ' ')
    frase_nova = frase_nova.replace('?', ' ')
    frase_nova = frase_nova.replace(',', ' ')
    frase_nova = frase_nova.replace('-', ' ')
    frase_nova = frase_nova.replace(':', ' ')
    frase_nova = frase_nova.replace('...', ' ')
    frase_nova = frase_nova.replace(';', ' ')
    return frase_nova

def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    nova_frase = retira_pontuacao(frase)
    nova_frase = nova_frase.split(' ')
    nova_frase = nova_frase[::-1]
    return str(nova_frase)