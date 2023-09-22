def retira_pontuacao(frase):
    '''retorna a frase informada com todos os caracteres de pontuação substituidos por um espaço
    str -> str'''
    travessao = str.replace(frase,'-',' ')
    virgula = str.replace(frase,',',' ')
    dois_pontos = str.replace(frase,':',' ')
    ponto_virgula = str.replace(frase,';',' ')
    ponto = str.replace(frase,'.',' ')
    exclamacao = str.replace(frase,'!',' ')
    interrogacao = str.replace(frase,'?',' ')
    frase_final = travessao + virgula + dois_pontos + ponto_virgula + ponto + exclamacao + interrogacao