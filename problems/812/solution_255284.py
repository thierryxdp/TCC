def retira_pontuacao (frase):
    """Função que, dada uma frase, retorna a mesma com todos os caracteres substituídos por um espaço
    entrada: str
    saída: str"""
    
    x = str.replace(frase, '-', ' ')
    y = str.replace(x, ',', ' ')
    z = str.replace(y, ':', ' ')
    w = str.replace(z, ';', ' ')
    u = str.replace(w, '.', ' ')
    t = str.replace(u, '?', ' ')
    p = str.replace(t, '!', ' ')
    q = str.replace(p, '...', ' ')
    
    return q