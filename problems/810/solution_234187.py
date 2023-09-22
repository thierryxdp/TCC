def inverte (frase):
    """Faça uma função que dada uma frase retorne outra frase com as palavras da frase de entrada na ordem inversa, sem letras maiúsculas e sem pontuação.
    Exemplo: "Nossa, como eu gosto de chocolate" com a frase inversa -1 retorna "chocolate de gosto eu como nossa". """
   
    lista = str.split(frase, "/") 
    frase = frase.lower()
    antes = frase(inverte)
    lista = frase (inverte[-1])
    frase = str.join (frase, lista)
    print (lista)
    return lista [-1]