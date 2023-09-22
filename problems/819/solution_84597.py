# Questão 1
def filtraMultiplos (lista,n):
    '''Função que nos retornará listas com os números multiplos de n'''
    
    listas_finais = []
    numero = 0
    
    while numero<len(lista):
        #enquanto  o contador for menor que o tamanho da lista
        
        if (lista[numero]%n) == 0:
            #se o número que estará na posição tiver resto 0 se dividido por n
            
            listas_finais = listas_finais + [lista[numero]]
                # ele será adicionádo à lista final
                
        numero += 1
            #no final ele adiciona 1 para ir para o próximo elemento
        
    return listas_finais