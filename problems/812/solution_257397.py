def retira_pontuacao(frase):
    """Cálculo de uma função que dada uma frase retorne onde todos os caracteres de pontuação tenham sido substituidos por espaço.
    
       Parameters:
       frase: Frase onde serão retirados os caracteres e substituidos por espaço.
       
       Returns:
       Retorna a frase com espaços no lugar das pontuações dado que:
       str -> str  
    """
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"."," "),","," "),";"," "),":"," "),"_"," "),"!"," "),"?"," "),"-"," ")