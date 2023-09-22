#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
#include <stdio.h>

int main(void)
{
    int x[2][2],y[2][2];
0
    scanf("%d %d %d %d",&x[0][0],&y[0][0],&x[0][1],&y[0][1]);
    scanf("%d %d %d %d",&x[1][0],&y[1][0],&x[1][1],&y[1][1]);
    if (x[0][1] < x[1][0] || x[1][1] < x[0][0] || y[0][1] < y[1][0] || y[1][1] < y[0][0] || x[0][0] > x[1][1] || x[1][0] > x[0][1] || y[0][0] > y[1][1] || y[1][0] > y[0][1])
      printf("0\n");
    else printf("1\n");
    return(0);
# segunda etapa - calculo do resultado