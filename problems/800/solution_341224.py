def total(lista,mercado):
    
    total=0
    for i in range(len(lista)):
        total=total+mercado[lista[i]]
          
    return round(total,2)