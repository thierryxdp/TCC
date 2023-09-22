# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchão(A,B,C,H,L)

int A, B, C;
int H, L;

int check(int X, int Y) {
	return X <= H && Y <= L;
}

int main() {
	scanf("%d %d %d", &A, &B, &C);
	scanf("%d %d", &H, &L);

	int ok = check(A, B) || check(B, C) || check(C, A) ||
		     check(B, A) || check(C, B) || check(A, C);

	puts(ok ? "S" : "N");
	return 0;
}