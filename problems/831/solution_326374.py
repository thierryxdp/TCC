def lingua_p(palavra):
    vogais = "aeiou"
    traducao = []
    for letra in palavra:
        traducao.extend([letra] if letra in vogais else [letra, 'p', letra])
        
    return "".join(traducao)