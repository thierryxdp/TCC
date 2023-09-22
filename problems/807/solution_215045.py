def conta_frases(t):
    '''Função que tendo um texto como entrada retorna a quantidade de
    frases existentes nesse texto
    str -> int'''
    a= str.replace(t,'.','#')
    a= str.replace(a,'!','#')
    a= str.replace(a,'?','#')
    a= str.replace(a,'...','#')
    n= str.split(a,'#')
    esp= n.count('')
    return len(n) - esp