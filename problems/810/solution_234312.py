def inverte(frase):
    """função que dada uma frase retorne outra frase com as mesmas palavras porém sem letras maiúsculas e sem pontuação.
    Exemplo: "Nossa, como eu gosto de chocolate" com a frase inversa -1 retorna "chocolate de gosto eu como nossa ". """

   # -*- coding: utf-8: -*-
for x in frase.split():
    if len(x) > 3: 
        print x