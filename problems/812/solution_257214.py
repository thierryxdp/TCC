def retira_pontuacao(frase):
    """Função que dada uma frase retorna a frase onde todos os tipos de 
       pontuação como (travessão,vírgula,dois pontos,ponto e vírgula e 
       pontos finais) sejam substituidos por espaços.
       str->str
       
       Parâmetros: 
       frase: A frase que serão substituidos a pontuação por espaços.
       
       returns: A frase com sua pontuação substituida por espaços.
    """
    return str.replace(frase,"-"," ")+(frase,","," ")+(frase,":"," ")+(frase,";"," ")+(frase,"..."," ")+(frase,"!"," ")+(frase,"?"," ")+(frase,"."," ")