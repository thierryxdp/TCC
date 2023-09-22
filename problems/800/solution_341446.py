def total(listadecompras,produtos):
    '''função que retorna o valor total dos itens da lista que 
    estejam disponíveis nesta loja;
    list,dict -> float'''
    
    
    for listadecompras in produtos:
       	soma = soma + mercado[listadecompras]
    return soma