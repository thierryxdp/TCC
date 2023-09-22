def retira_pontuacao (frase):
    """recebe uma frase e rotorna a mesma frase, só que com todos os caracteres de pontuação substituidos
    por espaço; str -> str"""
    a = str.replace(frase, '/','')
    b = str.replace(a, ',','')
    c = str.replace(b, ':','')
    d = str.replace(c, '.','')
    e = str.replace(d, '?','')
    f = str.replace(e, '!','')
    g = str.replace(f, '-', ' ')
    
    return g

def inverte (frase):
    """dada uma frase, a função retorna outra frase com as mesmas palavras da usada como parametro só que na ordem inversa. Porém,
    sem letras maiúsculas e sem pontuação; str -> str"""
    
    frase1 = retira_pontuacao(frase)
    frase2 = str.lower (frase1)
    B = str.split(frase2, ' ')
    reverso = B[::-1]
    return str.join(' ', reverso)