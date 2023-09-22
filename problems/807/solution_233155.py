def altera_frase(lista):
    """sdssds"""

    fraseA = lista[0]
    palavra = lista[1]
    posicao = lista[2]

    
    

    return fraseA

def altera_frase(frase,palavra,posicao):
    """Função que dado uma frase, uma palavra e uma posição,
    retorna a frase com a palavra dada como entrada em maiusculo caso ela
    ja esteja na frase, e se não, retorna a frase com a palavra na posição
    dada; lista -> string"""
    
    palavraB = str.upper(palavra,)
    fraseA = str.replace(frase,palavra+' ',palavraB+' ',1)
    
    fraseAux = str.split(frase)
    palavraB1 = [palavra]
    fraseB1 = fraseAux[0:posicao] + palavraB1 + fraseAux[posicao:]
    fraseB2 = str(fraseB1).strip('[]')
    fraseB3 = str.replace(fraseB2,',','')
    fraseF = str.replace(fraseB3,"'",'')
    fraseFF = str.strip(fraseF," ")
    

    if palavra in frase:
        return fraseA
    else:
        return fraseFF