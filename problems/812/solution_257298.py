def retira_pontuacao(frase):
    """Substirui todos os caracteres de pontuação por espaço.
       str->str
       
       Parameters:
       frase: A frase na qual os caracteres de pontuação serão substiuídos por espaços.
       
       Returns:
       Uma string onde em todas as posições que haviam caracteres de pontuação agora tem espaços.
       """
       return str.replace(str.replace(str.replace(str.replace(str.replace(frase,"."," "),","," "),";"," "),":"," "),"_"," ")