def inverte(frase):
    '''função que dada uma frase, remove toda a pontuação, deixa todas as letras em caixa baixa e retorna 
    a frase com as palavras em ordem invertida; str-> str'''
    frase = str.replace(frase,", "," ")
    frase= str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"/"," ")
    frase=str.split(frase, " ") 
    invertida = frase[-1::-1]
    frase_invertida=str.join(" ",invertida)
    minusculo=str.lower(frase_invertida)
    final=str.lstrip(minusculo, " ")
    return final