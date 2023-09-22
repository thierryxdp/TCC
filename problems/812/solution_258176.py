def retira_pontuacao(frase):
    '''Entre com uma frase para ser retornada a mesma porem, sem pontuacao
    String -> String'''

     x=frase.replace(".", " ")
     y=x.replace("!", " ")
        
     return y