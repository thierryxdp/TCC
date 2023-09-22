def quant_palavras(frase):
    """Função que recebe uma frase qualquer como parâmetro de entrada
    e retorna a quantidade de palavras presentes nessa frase.
    Entrada: str
    Saída: int
    """
    string_frase = str(frase)
    palavras = string_frase.split(" ")
    quantidade_palavras = len(palavras)
    
    return quantidade_palavras