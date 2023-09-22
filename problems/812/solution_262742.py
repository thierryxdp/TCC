def retira_pontuacao(Frase):
    """Função que retira as pontuações de uma determinada frase.
    Parâmetros de Entrada: Str
    Valor de Saída: Str"""
    
    Nova_Frase = Frase.replace("-"," ").replace(",","").replace(":","").replace(".","").replace(";","").replace("?","").replace("!","")
    return Nova_Frase

def inverte(Frase):
    """Função que inverte as palavras de uma 
    frase, retirando pontuação e sem letras maiúsculas.
    Parâmetros de Entrada: Str
    Valor de Saída: Str"""
    
    Frase = retira_pontuacao(Frase)
    Frase = Frase.lower()
    frase_final = frase.split(" ")
    fraseF = frase_final[::-1]
    return " ".join(fraseF).lstrip()