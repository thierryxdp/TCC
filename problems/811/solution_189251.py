#Questao 3
def colchao(medidas,H,L):
    """
Funcao que resolve o problema onde medidas é uma 
lista com os tamanhos inteiros A, B e C, e H e L
são os tamanhos inteiros da altura e largura da porta,
respectivamente.
    """
    int A, B, C;
    int H, L;

    int check(int X, int Y) {
	return X <= H && Y <= L;
}

int main() 
   {scanf("%d %d %d", &A, &B, &C);
	scanf("%d %d", &H, &L);

	int ok = check(A, B) || check(B, C) || check(C, A) ||
		     check(B, A) || check(C, B) || check(A, C);

	puts(ok ? "True" : "False");
	return 0;}