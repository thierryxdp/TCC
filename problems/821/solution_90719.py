def fatorial(valor):
    '''calcula e retorna o fatorial do valor
        int->int'''
    i=1
    valor_final=valor*i
    
    while i<valor:
        valor_final=valor_final*i
        i=i+1
      
    return valor_final