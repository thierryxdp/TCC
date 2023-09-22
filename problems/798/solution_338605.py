"""
Essa função recebe uma frase e retorna um dicionário com a frequência das palavras

Assinatura: str --> dict
"""

def freq_palavras(frases):
    
    """
    Primeiro eu reduzi a frase a apenas letras minúsculas e depois usei o "split" para separar a frase. Em seguida defini um dicionário e usei um laço de repetição "while"
    
    Dentro do laço foi testado se a palavra está ou não dentro do dicionário e se não estiver é adicionado e se estiver é adicionado +1 ao contador de frequência
    
    Por fim, o dicionário é retornado
    """
    
    frases = frases.lower()
    
    frases = frases.split(" ")
    
    dicionario = {}
    
    for i in range(len(frases)):
        
        if frases[i] not in dicionario:
            
            add = {frases[i]:1}
            
            dicionario.update(add)
            
        else:
            
            dicionario[frases[i]] = dicionario[frases[i]] + 1
            
    return dicionario