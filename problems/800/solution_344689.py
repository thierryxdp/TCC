def total(lista, produtos):
    despesa = 0
    
    for item in produtos:
            if lista in item:
                despesa = despesa + item
                
    print(despesa)