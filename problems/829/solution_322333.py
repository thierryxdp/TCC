def soma_h(n):
    """Retorna o resultado da soma 1 + 1/2 + ... + 1/n ;
    int --> float"""
    Bianca= 0
    for i in range (n):
        if i==0:
            Bianca+=0
        else:
            Bianca + =1 /i
            
      return round (Bianca + 1/n,2)