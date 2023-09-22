def transforma(frase, pontuacao):
    sem_pontuacao = frase.split(pontuacao)
    return ' '.join(sem_pontuacao)

def retira_pontuacao(frase):
    nova_frase = transforma(frase, '.')
    nova_frase = transforma(nova_frase, '!')
    nova_frase = transforma(nova_frase, '?')
    nova_frase = transforma(nova_frase, '-')
    nova_frase = transforma(nova_frase, ',')
    nova_frase = transforma(nova_frase, ';')
    return nova_frase

def inverte(frase):
    nova_frase = retira_pontuacao(frase)
    palavras = nova_frase.split(' ')
    return ' '.join(palavras[::-1])