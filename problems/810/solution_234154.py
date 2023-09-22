def retira_pontuacao(frase):
    pontuacao = ("/",",",":",";",".","?","!","...","'","(",")","-","{","}")

    nova_frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, "/", " "),","," "),":"," "),";"," "),"."," "),"?"," "),"!"," "),"..."," "),"'"," "),"("," "),")"," "),"-", " "),"{"," "),"}"," ")
    return nova_frase


def inverte(frase):
    """
    Inverte a ordem das palavras de uma frase, em letras minúsculas e sem
    pontuação.
    str -> str

    Parameters:
    frase: Parâmetro textual, do tipo string (str);
    
    Returns:
    Uma frase com as palavras em posições invertidas, onde todos os caracteres são minúsculos
    e todas as pontuações foram substituídas por espaço.
    """

    novo_texto = str.lower(retira_pontuacao(frase))
        
    x = novo_texto.split()
    nova_frase = x[::-1]
   
    return str.join(" ",nova_frase)