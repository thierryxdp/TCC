def retira_pontuacao(frase):
    
    """Funçao que recebe como parametro uma frase e retorna 
    a mesma porem com 'espaço' no lugar das pontuaçoes"""
    
    travessao=str.replace(frase,"-"," ")
    
    virgula=str.replace(travessao,","," ")
   
    dois_pontos=str.replace(virgula,":"," ")
    
    ponto_virgula=str.replace(dois_pontos,";"," ")
    
    ponto=str.replace(ponto_virgula,"."," ")
    
    exclamacao=str.replace(ponto,"!"," ")
    
    interrogacao=str.replace(exclamacao,"?"," ")
    
    frase_final=interrogacao
    
    return frase_final