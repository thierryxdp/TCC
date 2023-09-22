def retira_pontuacao(frase):
    frase=frase.eplace('!',' ').replace('?',' ').replace('...',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';' ' ')
    return frase
def inverte_frase(frase):
    'pega a frase e retorna ela minuscula,sem pontuacao e na ordem inversa...string---string'
    frases=retira_pontuacao(frase).lower().split(' ')[::-1]
    return ' '.join(frases)