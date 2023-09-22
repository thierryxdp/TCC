def substitui(s, x, i):
    """Função que retorna uma string igual a s, exceto que o elemento da posição i (int) deve ser substituído pelo caractere x
    (str, str, int) -> (str)"""


    return s[0: i] + x + s[(i+1):]


def teste_substitui():
    """Função que testa a veracidade da função substitui(s, x, i)"""
    
    print("particularista", "b", 4) == "partbcularista"
    print("repelir", "q", 5) == "repelqr"
    print("predilecção", "y", 1) == "pyedilecção"