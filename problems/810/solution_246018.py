def retira_pontuacao(texto):
    '''Dada uma frase, retorna essa mesma frase, só que com os caracteres de pontuação substituídos por espaço; str -> str'''

    texto = str.replace(texto,"."," ")
    texto = str.replace(texto,"?"," ")
    texto = str.replace(texto,"!"," ")
    
    texto = str.replace(texto,","," ")
    texto = str.replace(texto,";"," ")
    
    texto = str.replace(texto,"-"," ")
    texto = str.replace(texto,":"," ")
    
    texto = str.replace(texto,"..."," ")
    
    return texto

def inverte(texto):
    '''dada uma frase, retorna outra frase que contenha as mesmas palavras da frase de entrada, na ordem inversa, sem letras maiusculas e sem pontuação; str -> str'''

    texto = retira_pontuacao(texto)

    texto = str.lower(texto)
    
    lista = str.split(texto)
    list.reverse(lista)

    final = str.join(" ",lista)

    return final