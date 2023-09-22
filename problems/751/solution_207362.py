def quant_palavras(frase):
    """função que retorna quantas palavras uma frase possui, através da entrada "frase";
    Entrada: str
    Saída: int"""
    return (str.count(frase,' ',0,) - str.count(frase,' ',0,1) - str.count(frase,' ',-2,) + 1)