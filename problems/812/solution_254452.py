def retira_pontuacao(frase):
    """Função que calcula dada um str em frase de entrada retorna uma str sem todas as caracteres de pontação
    str -> str"""
    
    return frase.replace("?"," ").replace("..."," ").replace("!"," ").replace("."," ").replace(","," ").replace("-"," ")