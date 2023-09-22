def num_bombom(d,nb,p=2):
    "função que calcula o troco de pedrinho dado o dinheiro, o numero de bombons e o preço o preço pelo proprio pedrinho(float,int,float -> float)"
    x = nb*p
    t= d - x
    return "pedrinho comprou", nb ,"bombons, e o seu troco é",t,"reais."