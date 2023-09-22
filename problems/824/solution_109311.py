def uppCons(frase):
    """funcao que recebe como entrada uma frase e retorna a frase com todas
    	as consoantes em maiúsculas."""
    resposta=""
    for letra in frase:
        if letra not in {"a","e","i","o","u","á","é","í","ó","ú","ã","õ","â","ê","ô"}:
            resposta = resposta + letra.upper()
        else:
            resposta=resposta+letra
    return resposta