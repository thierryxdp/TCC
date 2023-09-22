def conta_frases(string):
    '''Função que dada a frase numa string,substitui todas as pontuações de exclamação,interrogação e reticências por ponto e retorna a quantidade de frases no texto que terminam nas pontuações
string> int'''


    s= string
    s=str.replace(s, '!', '.')
    s=str.replace(s, '?', '.')
    s=str. replace(s,'...', '.')
    
    

    x= str.count(s, '.')
   
    return x