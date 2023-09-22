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

def inverte(frase:str) -> str:
    """Esta função, dada uma frase como parâmetro de entrada,
    retorna outra frase com as mesmas palavras da frase de entrada
    na ordem inversa, sem letras maiúsculas e sem pontuação"""
    
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase = frase[::-1]
    frase = " ".join(frase)
    
    return frase