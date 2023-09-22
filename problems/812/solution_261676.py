def retira_pontuacao(texto):
    """Substitui todas as pontuações de um dado texto por espaços, retornando uma frase sem pontuação.
    Entrada: str
    Saída: str
    """
    A = str.replace (texto, '-', ' ')
    B = str.replace (A, ',', ' ')
    C = str.replace (B, ':', ' ')
    D = str.replace (C, ';', ' ')
    E = str.replace (D, '.', ' ')
    F = str.replace (E, '!', ' ')
    G = str.replace (F, '?', ' ')
    return G