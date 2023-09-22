def retira_pontuacao(frase):
    ''' Função que retorna uma frase com sua pontuação substiuída por espaços
    incluindo a pontuação de encerramento da frase.   str=> str'''
    pontucao = ['.','?','!',':',';','—',',']
    x = frase.replace(pontuacao,'')
    return x