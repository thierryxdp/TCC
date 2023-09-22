def retira_pontuacao (frase):
    """recebe uma frase e rotorna a mesma frase, só que com todos os caracteres de pontuação substituidos
    por espaço. Para fazer isso a função substitui todos as pontuações dadas pelo enunciado e substitui por um espaço
    vazio atráves de str.replace; 
    str -> str"""
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
    sem letras maiúsculas e sem pontuação. Para retirar os pontos da frase que deve ser invertida usa-se o 'retira_pontuação()',
    da função anterior. Após isso, torna todas as letras da frase minusculas através do str.lower. Agora só é preciso inverte-la, para
    isso é preciso dividir todas as palavras da strings e depois inverte-la. Com isso em mente, a função usa str.split separando as palavras
    a cada espaço entre elas e entã inverte-a atráves do fatiamento [::-1]. Porém, na conversão para lista (str.split) a frase se separou em vários
    indices separados por virgula, logo, usa-se a str.join para retornar o resultado final.; str -> str"""
    
    frase1 = retira_pontuacao(frase)
    frase2 = str.lower (frase1)
    B = str.split(frase2, ' ')
    reverso = B[::-1]
    return str.join(' ', reverso)