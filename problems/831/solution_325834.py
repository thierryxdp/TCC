# Dada uma palavra, esta função retorna a palavra equivalente na língua do P,
# como explicado no enunciado.
# str -> str

def lingua_p(palavra):
    resposta =''
    
    palavra = str.lower(palavra)
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóúâêîôûãõ':
            resposta = resposta + palavra[i] + 'p' + palavra[i]
        else:
            resposta = resposta + palavra[i]
            
    return resposta