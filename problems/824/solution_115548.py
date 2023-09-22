def uppCons (frase):
    """
    	Função que retorna a frase dada com suas consoantes
        maiusculas.
    	string -> string
    """
    alfabeto = ['A','b','c','d','E','f','g','h','I','j','k','l','m','n','O','p','q','r','s','t','U','v','w','x','y','z']
    i = 0
    maiusculas = ''
    while frase[i] in alfabeto:
         maiusculas = frase[0:i]+frase[i].upper()+frase[i-1:]
    i = 0 + 1
    return maiusculas