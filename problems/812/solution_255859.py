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