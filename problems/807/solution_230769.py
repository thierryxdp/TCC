def conta_frases(texto):

    texto_2=str.replace(texto,"...",".")
    
    ponto_final=str.count(texto_2,".",0,len(texto))
    
    ponto_exclamacao:str.count(texto_2,"!",0,len(texto))
        
    ponto_interrogacao:str.count(texto_2,"?",0,len(texto))
        
    return ponto_final+ponto_exclamacao+ponto_interrogacao
'''funcao que dada um texto armazenado em uma string, conta o numero de frases que esse texto possui.
entrada:str
saida:int'''