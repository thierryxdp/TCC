def retira_pontuacao (frase):
    """recebe uma frase e rotorna a mesma frase, só que com todos os caracteres de pontuação substituidos
    por espaço. Para fazer isso a função substitui todos as pontuações dadas pelo enunciado e substitui por um espaço
    vazio atráves de str.replace; 
    str -> str"""
    a = str.replace(frase, '/',' ')
    b = str.replace(a, ',',' ')
    c = str.replace(b, ':',' ')
    d = str.replace(c, '.',' ')
    e = str.replace(d, '?',' ')
    f = str.replace(e, '!',' ')
    g = str.replace(f, '-', ' ')
    
    return g