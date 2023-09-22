def conta_frases(frase: str) -> int:
    """Esta função, dada uma string com frases separadas por pontuações
    (., !,?,...) como parâmetro de entrada, calcula e retorna o
    número de frases na string."""
    
    #Substituindo todos as pontuações por # para usá-la como separador de frases
    frase = frase.replace("...", "#")
    frase = frase.replace("?", "#")
    frase = frase.replace(".", "#")
    frase = frase.replace("!", "#")
    
    #Contando quantas frases existem na string através do separador "#"
    conta_frases = frase.count('#')
    
    return conta_frases