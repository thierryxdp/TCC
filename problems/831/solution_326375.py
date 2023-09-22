def lingua_p(palavra):
    consoantes = "bcdfghjklmnopqrstvwxz"
    traducao = []
    for letra in palavra:
        traducao.extend([letra] if letra in consoantes else [letra, 'p', letra])
        
    return "".join(traducao)