def posLetra(conteudo_str,letra,num_ocorrencia):
    '''
    Função que retorna a posição, dentro da string, da ocorrência desejada 
    de uma letra, após receber a string a letra e o número de tal ocorrência.
    str,str,int -> int
    '''
    if conteudo_str.count(letra) < num_ocorrencia:
        return -1
    else:
        contador = 0
        list_letras = []
        elem_frase = list(conteudo_str)
        while contador < len(elem_frase) and len(list_letras) < num_ocorrencia:
            if letra == elem_frase[contador]:
                list.append(list_letras, elem_frase[contador])
            contador = contador + 1
        return contador - 1