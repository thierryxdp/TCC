def total(listadecompras,produtos):
    '''função que retorna o valor total dos itens da lista que 
    estejam disponíveis nesta loja;
    list,dict -> float'''
    
    soma = 0
    i = 0
    
    for listadecompras in produtos:
       	soma = soma + produtos[listadecompras[i]]
    i = i + 1
    
    return soma