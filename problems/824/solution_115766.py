def uppCons(frase):
    "Função que recebe uma frase como entrada e retorna a frase com todas as consoantes em maiúculo. Entrada: str; Saída: str"
    letras = 'aeiouAEIOUãáàéèíõóú'
    palavras=''
    i=0
    while i<len (frase):
        if frase[i] not in letras:            
            palavras= palavras + str.upper(frase[i])
        else:
            palavras = palavras+ frase[i]
        i=i+1
    return palavras