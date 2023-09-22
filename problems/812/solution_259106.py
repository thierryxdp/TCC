def retira_pontuacao(frase:str) -> str:
    """Esta função, dada uma frase como parâmetro de entrada,
    retorna a frase onde todos os caracteres de pontuação
    foram substituidos por espaço"""
    
    frase = frase.replace("-", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace("?", " ")
    
    return frase