def faltante(faltando):
    ''' Dada uma lista com os numeros de todas as pecas de quebra-cabeca que 
    se possui (considerando que uma esta faltando) a funcao retorna qual o
    numero da peca que falta;
    
    list -> int '''
    
    # arrumar  a lista dada em ordem crescente
    list.sort(faltando)
    
    # adicionar um elemento pra completar a lista faltante
    list.append(faltando,0)
    
    # descobrir quantas pecas deveria ter o quebra-cabeca
    total_pecas = len(faltando)
    
    # lista com todas as pecas do quebra_cabeca completo
    completo = list(range(1,total_pecas + 1))
    
    # numero da peca que ele tem pra comparar com o numero na lista completa
    ele_tem = faltando[0]
    nao_tem = completo[0]
    
    indice = 0
    
    # comparar se a peca que ele tem bate com a peca da lista completa
    while ele_tem == nao_tem:
        
        indice += 1
        
        ele_tem = faltando[indice]
        nao_tem = completo[indice]
        
    return nao_tem