import numpy as np
def posLetra(string, let, n):
    """Recebe stringm uma letra e um valor que indica a ocorrência da letra, retornando
    a posição dela na string.
    """
    indic=[string.index(let) for let in string]