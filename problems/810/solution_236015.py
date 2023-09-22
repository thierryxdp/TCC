def retira_pontuacao1(frase):
    """Recebe uma frase e retorna uma nova onde todas as pontuações estão
    trocadas por espaços"""
    frase = frase.lower()
    frase_nova = frase.replace('.', '')
    frase_nova = frase_nova.replace('!', '')
    frase_nova = frase_nova.replace('?', '')
    frase_nova = frase_nova.replace(',', '')
    frase_nova = frase_nova.replace('-', '')
    frase_nova = frase_nova.replace(':', '')
    frase_nova = frase_nova.replace('...', '')
    frase_nova = frase_nova.replace(';', '')
    return frase_nova

def inverte(frase):
    """Recebe uma frase e inverte a ordem de suas palavras"""
    nova_frase = frase.split()
    nova_frase = nova_frase[::-1]
    nova_frase = str.join('', nova_frase)
    nova_frase = retira_pontuacao1(nova_frase)
    return nova_frase