def retira_pontuacao(F):
    """Funcao que dada uma frase F retorna a frase onde todos
    os caracteres de pontuacao(incluindo travessao, virgula,
    dois pontos, ponto e virgula, alem da pontuacao de 
    encerramento da frase) sao substituidos por espaco;
    str->str"""
    
    Semtravessao=str.replace(F,"-"," ")
    Semvirgula=str.replace(Semtravessao,","," ")
    Semdoispontos=str.replace(Semvirgula,":"," ")
    Sempontoevirgula=str.replace(Semdoispontos,";"," ")
    Semexclamacao=str.replace(Sempontoevirgula,"!"," ")
    Seminterrogacao=str.replace(Semexclamacao,"?"," ")
    Semreticencias=str.replace(Seminterrogacao,"..."," ")
    
    return str.replace(Semreticencias,"."," ")