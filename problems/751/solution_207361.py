def quant_palavras(frase):
    """função que retorna quantas palavras uma frase possui, através da entrada "frase";
    Entrada: str
    Saída: int"""
    return (str.count(texto,' ',0,) - str.count(texto,' ',0,1) - str.count(texto,' ',-2,) + 1)