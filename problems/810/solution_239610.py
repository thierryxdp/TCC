def inverte(F):
    """Funcao que dada uma frase F retorna uma outra frase 
    que contêm as mesmas palavras da frase de entrada na 
    ordem inversa, sem letras maiusculas, e sem pontuacao;
    str->str"""
    
    Semtravessao=str.replace(F,"-"," ")
    Semvirgula=str.replace(Semtravessao,",","")
    Semdoispontos=str.replace(Semvirgula,":"," ")
    Sempontoevirgula=str.replace(Semdoispontos,";"," ")
    Semexclamacao=str.replace(Sempontoevirgula,"!","")
    Seminterrogacao=str.replace(Semexclamacao,"?","")
    Semreticencias=str.replace(Seminterrogacao,"...","")
    Sempontofinal=str.replace(Semreticencias,".","")
    Separacaodepalavras=str.split(Sempontofinal," ")
    Inversao=Separacaodepalavras[::-1]
    Juncaodepalavras=str.join(" ",Inversao)
    
    return str.lower(Juncaodepalavras)