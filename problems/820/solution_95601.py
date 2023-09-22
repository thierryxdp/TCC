def posLetra(string, letra, n):
    'Dada uma string, letra e número (n); retorna a posição da n ocorrência da letra na string. Caso exista menos ocorrências, retorna -1. Entrada: str,str,int. Saída: int.'
    if (letra in string and n<=str.count(string,letra)):
        indice=0
        incidencia=0
        frase=str.split(str.join('*',string),'*')
        resultado=0
        while ((indice<len(frase)) and incidencia<n):
            if frase[indice]==letra:
                incidencia=incidencia+1
                resultado=índice
            indice=indice+1
        return resultado
        
    else:
            return -1