def transforma(frase, pontuacao):
    sem_pontuacao = frase.split(pontuacao)
    return ' '.join(sem_pontuacao)

def retira_pontuacao(frase):
    nova_frase = transforma(frase, '.')
    nova_frase = transforma(frase, '!')
    nova_frase = transforma(frase, '?')
    nova_frase = transforma(frase, '-')
    nova_frase = transforma(frase, ',')
    nova_frase = transforma(frase, ';')
    return nova_frase