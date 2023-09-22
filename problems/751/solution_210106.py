def quant_palavras(frase):
  
    contagem = frase.split()
    return len(contagem)
    
print quant_palavras("Welcome to the jungle")