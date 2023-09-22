# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def retira_pontuacao(frases):
    '''Retorna frase sem pontuação.
    str->str'''
    frase_sem_pontuacao=''
    for caractere in frases:
        if caractere not in '-,.;:?!':
            frase_sem_pontuacao= frase_sem_pontuacao + caractere
    return frase_sem_pontuacao

def freq_palavras(frases):
    d={}
    frases_sem_pontuacao=retira_pontuacao(frases)
    palavras=str.split(frases_sem_pontuacao)
    for palavra in palavras:
        d[palavra]=list.count(palavras,palavra)
    return d