def retira_pontuacao(frase):
    """Funcao que dada uma frase retorna a frase com todos os caracteres 
          de pontuacao subistituidos por espaco."""'
    pontuacao = ['!', '?','.', '-']
    for trocar in pontuacao:
        frase=frase.replace(trocar,' ')
        return frase