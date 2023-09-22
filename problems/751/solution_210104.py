def conta_palavras(frase):
  
    frase = str.split(frase)
    return len(frase)
    
print conta_palavras("Welcome to the jungle")