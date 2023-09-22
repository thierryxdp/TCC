def posLetra(frase, letra, num=0):
    '''Faça uma função posLetra que recebe como entrada uma 
  string, uma letra, e um n umero que indica a ocorrencia 
  desejada da letra (1 para primeira ocorrencia, 2 para segunda, etc).
  Sua função deve retornarem que posição da string aquela 
  ocorrencia da letra esta. Caso exista menos ocorrencias 
  da letra do que a ocorrencia pedida, 
  a funcao deve retornar -1. str,str,int - > int
    '''
int conta char (char* str, char letra);
i n t c o n t a c h a r ( char∗ s t r , char l e t r a )
{
i n t i =0, con ta=0;
wh i le ( s t r [ i ] != 0) {
i f ( s t r [ i ] == l e t r a ) {
con ta++;
}
i++;
}
re turn con ta ;
}
i=0
x=0
while frase[i] !=0:
    if frase[i] == letra:
        x=+1
    else:
        i=+1
if num <= len(letra):
    return x