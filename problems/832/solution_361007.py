soma = 0;
    for(l = 0; l < tam; l++){ // soma da diagonal secundária
        soma += mat[l][tam - 1 - l];
    }
    printf("Diag. secundaria: %d\n", soma);

    if(total != soma)
        printf("Diagonal secundaria eh diferente!\n");

    for(l = 0; l < tam; l++){ // soma da linhas
        soma = 0;
        for(c = 0; c < tam; c++)
            soma += mat[l][c];
        printf("Linha %d: %d\n", l, soma);

        if(total != soma){
            printf("Linha %d eh diferente\n", l);
            falha++;
        }
    }

    for(c = 0; c < tam; c++){ // soma das colunas são iguais
        soma = 0;
        for(l = 0; l < tam; l++)
            soma += mat[l][c];
        printf("Coluna %d: %d\n", c, soma);

        if(total != soma){
            printf("Coluna %d eh diferente\n", c);
            falha++;
        }
    }

    if(falha == 0)
        printf("\nHe um quadrado magico!!!!\n");

    return 0;
}