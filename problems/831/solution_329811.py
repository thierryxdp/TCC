def lingua_p (palavrinha):
'''s seguinte função irá receber uma palavra em 
português e assim irá retornar a mesma traduzida na 
língua do p. str--> str'''
    
    traduzido_p = []
contado = 0
for letra in list(palavrinha):
    if letras in áéíóú aeiou:
        traduzido_p.append(letras + 'p' + letras)
    else:
        traduzido_p.append(letras)
        return ''.join(traduzido_p)