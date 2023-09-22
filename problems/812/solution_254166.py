def retira_pontuacao(frase):
    """
    Substitui todas as pontuações de uma frase por um espaço.
    str -> str

    Obs: Adotar-se-á como pontuação os seguintes caracteres:
    # Barra, vírgula, dois pontos, ponto e vírgula, ponto de interrogação,
    ponto de exclamação, reticências, aspas, parênteses, travessão e colchetes.
    
    Parameters:
    frase: Parâmetro textual, do tipo string (str);
    
    Returns:
    Uma frase modificada, onde todos os caracteres de pontuação foram substituídos
    por espaço.
    """
    pontuacao = ("/",",",":",";",".","?","!","...","'","(",")","-","{","}")

    nova_frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, "/", " "),","," "),":"," "),";"," "),"."," "),"?"," "),"!"," "),"..."," "),"'"," "),"("," "),")"," "),"-", " "),"{"," "),"}"," ")
    return nova_frase