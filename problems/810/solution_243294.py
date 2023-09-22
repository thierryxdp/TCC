#Exercício_05:
''' Essa função insere um número "n" numa lista de forma tal que ela contínua ordenada de maneira crescente. '''
''' list, float ---> list. '''

def insere(string_text):
    
    #Tirando a pontuação:
    a = str.replace(string_text, ",", "")
    
    b = str.replace(a, ".", "")
    
    c = str.replace(b, "?", " ")
    
    d = str.replace(c, "!", " ")
    
    e = str.replace(d, "-", " ")
    
    f = str.replace(e, ":", " ")
    
    g = str.replace(f, ";", " ")
    
    #Retirando as letras maiúsculas:
    h = str.lower(g)
    
    #Transformando a frase em lista:
    i = list(h)
    
    #Revertendo a lista:
    list.reverse(i)
    
    #Retornando:
    return i

insere('Olá! como você vai? aqui tudo bem, graças a Deus.')