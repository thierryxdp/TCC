def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
	pontuacao = ['-',',',':',';','.','!','?']
    if 'pontuacao' in frase:
        return str.replace(frase,'pontuacao',' ')