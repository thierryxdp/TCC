def retira_pontuacao(frase):
    """Funcao que recebe uma frase e retorna a frase trocando todas as pontuacoes por espaço. str=>str"""
    frase=  str.replace(frase,'.',' ')
    frase=  str.replace(frase,'?',' ')
    frase=  str.replace(frase,'!',' ')
    frase=  str.replace(frase,',',' ')
    frase=  str.replace(frase,':',' ')
    frase=  str.replace(frase,';',' ')
    frase=  str.replace(frase,'-',' ')
    return frase