def retira_pontuacao(frase):
    """retorna a frase dada sem os caracteres de pontuação, com espaços no lugar
       ,incluindo travessão,vírgula,dois pontos, ponto e vírgula
       string->string"""
    return str.replace(str.replace(frase,"-"," "),"!"," ")