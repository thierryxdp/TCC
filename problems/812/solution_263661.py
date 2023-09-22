def retira_pontuacao(frase):
    """
    
    funcao que dada uma frase pontuada, remove a pontuação (travessao, virgula, dois pontos, ponto e virgula e 
    ponto final), substituindo por espaço. frase-->str return
  
    :param frase: str 
    :return: str
    """
    
    ponto_virgula= frase.replace('-', ' ')
    virgula = ponto_virgula.replace(',', ' ')
    travessao = virgula.replace('-', ' ')
    dois_pontos = travessao.replace(':', ' ')
    ponto_interrogacao = dois_pontos.replace('?', ' ')
    ponto_exclamacao =ponto_interrogacao.replace('!', ' ')
    ponto_final = ponto_exclamacao.replace('.', ' ')
    
    
  
    
   
    return ponto_final