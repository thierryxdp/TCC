def retira_pontuacao(frase):
    """retorna a frase com substituindo a pontuação por espaço
Parametros:
Entrada:str
Saida:str"""
    frase=frase.replace("!"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ").replace("-"," ")
			
        return frase