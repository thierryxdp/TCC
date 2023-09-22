def inverte(frase):
    '''
    funcao que utiliza a frase dada retorne uma 
    outra frase que contenha as mesmas palavras
    na ordem inversa, sem letras maiusculas e pontuacao
    '''
    a= str.join(' ', str.split(frase, '.'))
    b= str.join(' ', str.split(a, ','))
    c= str.join(' ', str.split(b, '?'))
    d= str.join(' ', str.split(c, '!'))
    e= str.join(' ', str.split(d, '-'))
    retorno= e.split(' ')
    retorno2= retorno[-1:-(len(retorno)+1):-1]
    junto= str.strip(str.join(' ', retorno2))
    
    return str.lower(junto)