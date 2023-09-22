def inverte(frase):
    
    """Funçao que, dada uma frase retorna uma outra frase que contenha as mesmas palavras
    da frase de entrada na ordem inversa, sem letras maiusculas, e sem a pontuaçao."""
    
    travessao=str.replace(frase,"-"," ")
    
    virgula=str.replace(travessao,","," ")
    
    dois_pontos=str.replace(virgula,":"," ")
    
    ponto_virgula=str.replace(dois_pontos,";"," ")
    
    ponto=str.replace(ponto_virgula,"."," ")
    
    exclamacao=str.replace(ponto,"!"," ")
    
    interrogacao=str.replace(exclamacao,"?"," ")
    
    frase_final=interrogacao
    
    return frase_final