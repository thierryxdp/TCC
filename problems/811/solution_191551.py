import java.io.IOException;
import java.util.Scanner;

public class URI 2409 {
	
    public static void main(String[] args) throws IOException {
		Scanner leitor = new Scanner(System.in);
		int A = leitor.nextInt();
		int B = leitor.nextInt();
		int C = leitor.nextInt();
		int H = leitor.nextInt();
		int L = leitor.nextInt();
		
		     if (A <= H && B <= L) System.out.println("S");
		else if (A <= H && C <= L) System.out.println("S");
		else if (B <= H && A <= L) System.out.println("S");
		else if (B <= H && C <= L) System.out.println("S");
		else if (C <= H && A <= L) System.out.println("S");
		else if (C <= H && B <= L) System.out.println("S");
		else					   System.out.println("N");# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis