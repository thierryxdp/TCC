def retira_pontuacao(frase):
    
    """Funçao que dada uma frase, retorna a mesma onde todos os caracteres
    de pontuaçao(travessao, virgula, dois pontos, ponto e virgula), além da 
    pontuaçao final sejam substituidos por espaço"""
    
    travessao=str.replace(frase,"-"," ")
    
    virgula=str.replace(travessao,","," ")
    
    dois_pontos=str.replace(virgula,":"," ")
    
    ponto_virgula=str.replace(dois_pontos,";"," ")
    
    ponto=str.replace(ponto_virgula,"."," ")
    
    exclamacao=str.replace(ponto,"!"," ")
    
    interrogacao=str.replace(exclamacao,"?"," ")
    
    frase_final=interrogacao
    
    return frase_final