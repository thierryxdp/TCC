def lingua_p(palavra):
    """Essa função retorna a palavra dada modificada na língua do p.
    Como entrada temos uma palavra e com saída temos a palavra modificada;
    str->str"""
    lista=[]
    indice=0
    separacao=""
    while indice<len(palavra):
        indice+=1
        for i in palavra:
            if  i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=="Á" or i=="É" or i=="Í" or i=="Ú" or i=="Ó" or i=="á" or i=="é" or i=="í" or i=="ú" or i=="ó":
                novapalavra=i+"p"+i
                list.append(lista,novapalavra)
            else:
                list.append(lista,i)
        return separacao.join(lista)