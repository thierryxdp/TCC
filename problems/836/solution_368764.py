def busca(setor,matriz):
    """Funcao calcula e retorna um buca pela matriz por cada setor ou dado todos os
    funcionarios que retorna o setor a que pertence;
    string,list->list"""
    encontrados=[]
    for func in matriz:
        if setor in func[2]:
            encontrados.append(func[:2]+func[3:])
    return encontrados