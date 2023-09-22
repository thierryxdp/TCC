def posLetra(string, letra, n):
    'Dada uma string, letra e número (n); retorna a posição da n ocorrência da letra na string. Caso exista menos ocorrências, retorna -1. Entrada: str,str,int. Saída: int.'
    if letra in string:
        repeticoes=str.count(string,letra)
        if repeticoes<n:
            return -1
        else:
            indice=0
            incidencia=0
            frase=str.join(string,'')
            resultado=0
            while ((indice<len(frase)) and incidencia<n):
                if frase[indice]==letra:
                    incidencia=incidencia+1
                    resultado=resultado+indice
                indice=indice+1
            return indice