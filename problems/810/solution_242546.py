def retira_pontuacao(frase):
    """Atribui a frase recebida a outra variável e modifica esta última,
    substituindo toda pontuação por espaços.
    str-> str"""
    frase_nova=frase
    frase_nova=frase_nova.replace("..."," ")
    frase_nova=frase_nova.replace("."," ")
    frase_nova=frase_nova.replace("!"," ")
    frase_nova=frase_nova.replace("?"," ")
    frase_nova=frase_nova.replace("-"," ")
    frase_nova=frase_nova.replace("-"," ")
    frase_nova=frase_nova.replace(","," ")
    frase_nova=frase_nova.replace(":"," ")
    frase_nova=frase_nova.replace(";"," ")
    return frase_nova

def inverte(frase):
    """Atribui a frase recebida a outra variável e passa a modificar esta última.
    Primeiramente, usa a função retira_pontuação para retirar a pontuação dela,
    após isso utiliza a função lower para retirar as maiúsculas, por último
    divide a frase nos espaços pela função split em uma lista para inverter a lista
    e unir com a função join as palavras novamente,
    str-> str"""
    frase_invertida=frase
    frase_invertida=retira_pontuacao(frase_invertida)
    frase_invertida=frase_invertida.lower()
    frase_invertida=frase_invertida.split()
    frase_invertida=frase_invertida.reverse()
    frase_invertida=str.join(" ",frase_invertida)
    return frase_invertida