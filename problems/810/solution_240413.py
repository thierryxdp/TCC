import copy
def inverte(frase):
    
    copia=copy.deepcopy(frase)
    
    copia.replace("!"," ").replace("?"," ").replace("."," ").replace(";"," ").replace("-"," ").replace(":"," ").replace(","," ")
    
    copia.split()
    
    return copia