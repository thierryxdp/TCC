def inverte(s):
    """A função dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entredan orddem inversa.
    Assinatura: str -> str"""
    str = "" 
    for i in s: 
      str = i + str
    return str
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (inverte(s))