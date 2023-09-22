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

def inverte (frase):
    """Função que, dada uma frase, retorna um outra frase com as mesmas palavras da entrada, porém com ordem inversa, sem letras maiúsculas, e sem a pontuação.
    entrada: str
    saída: str"""
    
    pont = retira_pontuacao (frase)
    lista = str.split (pont, ' ')
    inversa = lista[::-1]
    juncao = str.join(' ', inversa)
    
    return juncao