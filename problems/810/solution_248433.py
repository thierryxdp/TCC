def  inverte ( frase ):
    "função que dada uma frase retorne uma outra frase que contenha as mesmas da frase de entrada na ordem inversa."
    lista  =  str . divisao ( frase )
    lista . reverso ()
    frase  =  str . juntar ( "" , lista )
     return (frase)