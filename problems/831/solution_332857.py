"""
A função recebe uma palavra em português e retorna a "tradução" dela na língua P

Assinatura: str --> str
"""

def lingua_p(palavra):
    
    """
    Para essa função eu criei uma lista "vogais" onde eu inclui as vogais e uma string vazia que será a tradução. Depois disso eu coloquei todas as letras em minúsculos usando "lower" e transformei a string numa lista para facilitar a função
    
    Em seguida a função entra num laço for que testa se a letra é vogal ou não, se for é adicionado um "p" e no fim retorna a tradução da palavra
    """
    
    vogais = ["a","e","i","o","u"]
    nova_palavra = ""
    
    palavra = palavra.lower()
    palavra = list(palavra)
    
    for i in range(len(palavra)):
        
        if palavra[i] in vogais:
            
            nova_palavra = nova_palavra + palavra[i] + "p" + palavra[i]
            
        else:
            
            nova_palavra = nova_palavra + palavra[i]
        
    nova_palavra = str(nova_palavra)
    
    return nova_palavra