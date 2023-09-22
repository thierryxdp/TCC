def soma_h(n):
    """
    Função que calcula e retorna o valor da soma h, com n termos, sendo n um número inteiro fornecido. forncecido
    A soma h tem a seguinte forma:
    h = 1+(1/2)+(1/3)+...+(1/n)
    """
    soma=0
    
    for i in range(1, n+1):
        
      
            somar += (1.0 / i+1)
            
        
                
    return round(somar,2)