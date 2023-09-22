def lingua_p(palavra):
    """Essa função retorna a palavra dada modificada na língua do p.
    Como entrada temos uma palavra e com saída temos a palavra modificada;
    str->str"""
    lista=[]
    indice=0
    separacao=""
    while indice<len(palavra):
        indice+=1
        vogais="AEIOUaeiouáéíóúÁÉÍÓÚ"
        for i in palavra:
            if i in vogais:
                novapalavra=i+"p"+i
                list.append(lista,novapalavra)
            else:
                list.append(lista,i)
        return separacao.join(lista)