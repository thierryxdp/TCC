def lingua_p(palavra):
    "recebe uma palavra e retorna ela, duplicando uma vogal com um P entre elas"
    "entrada: str. saida:str"
    palavra=str.lower(palavra)
    L=list(palavra)
    P=''
    for letra in L:
        if letra not in "qwrtypsdfghjklçmnbvcxz":
            P=P+letra+"p"+letra
        else:
            P=P+letra
    return  P