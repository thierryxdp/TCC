def primo(n):
    """Retorna se um numero é primo ou não. (int->bool)"""
     divisores=0
     for i in range(n):
         if n%(i+1)==0:
            divisores+=1
     if divisores<=2:
         return True
     else: 
         return False