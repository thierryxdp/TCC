def posLetra(texto,letra,num_oc):
    """Função que fornece o número da posição de uma letra na frase mencionada
       str,str,int ~> int"""
    if str.count(texto,letra) > num_oc:
        return -1