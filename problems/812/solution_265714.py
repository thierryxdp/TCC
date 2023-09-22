def retira_pontuacao(x):
    """Função que recebe uma frase e retorna a frase onde
todos os caracteres de pontuação foram substituidos por espaço .
    str -> str"""
    if "!" in x:
        x=str.replace(x,"!"," ")
    
    if "..." in x:
        x=str.replace(x,"..."," ")
    
    if "?" in x:
        x=str.replace(x,"?"," ")
    
    if "." in x:
        x=str.replace(x,"."," ")

    if "-" in x:
        x=str.replace(x,"-"," ")

    if "," in x:
        x=str.replace(x,","," ")

    if ";" in x:
        x=str.replace(x,";"," ")

    if ":" in x:
        x=str.replace(x,":"," ")
     
    return x