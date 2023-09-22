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
    '''explicação'''
    
    texto = str.lower(texto)
    
    lista = str.split(texto)
    
    return reverse(lista)