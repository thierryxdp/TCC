#Recebe uma frase
#Remove os caracteres de pontuação 
#retorna a frase
def retira_pontuacao(frase: str) -> str:
    """Recebe uma frase e retorna sem a pontuação"""
    FraseSemPontos=str.replace(str.replace(str.replace(str.replace
    (str.replace(str.replace(str.replace(frase, "-", " ")
     , "!", " "), ","," "), "."," "), "?", " "), ":", " "), ";", " ")
    return FraseSemPontos