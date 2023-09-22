def lingua_p(palavra):
    consoantes = "bcdfghjklmnpqrstvwxz"
    traducao = []
    for letra in palavra:
        traducao.extend([letra] if letra in consoantes else [letra, 'p', letra])
        
    return "".join(traducao)