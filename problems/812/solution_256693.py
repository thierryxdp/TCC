def retira_pontuacao(frase):
    '''Funcao que recebe uma frase e substitui todas as pontuacoes por espaco;
    str -> str'''
    especias = ['!', '?', '#', '$', '@', '%', '&', '*', ',', '.', '-']
    for trocar in especias:
        frase = frase.replace(trocar,' ')
    return frase