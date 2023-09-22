def inverte(frase):
    '''função que dada uma frase retorna uma outra frase que 
     contenha as mesmas palavras da frase de entradada na ordem iversa,
     sem letras maiúsculas, e sem a pontuação; str -> int'''
    pont1= str.count(frase,'!')
    pont2= str.count(frase,'?')
    pont3= (str.count(frase,'.'))-((str.count(frase,'...'))*3)
    ret= str.count(frase,'...')
    return pont1 + pont2 + pont3 + ret