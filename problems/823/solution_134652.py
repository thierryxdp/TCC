def falante(lista):

int somarN(int n){//somar n : ex se n=5 faça 1+2+3+4+5
    
    if(n==1)
    return n;    
    else    
    return n+somarN(n-1);
        
}

int pecaQuebraCabeca(int vet[],int n){
    int a,b,t;
    int x;
    int s=0;        
    
    x=n+somarN(n-1);// chama a funcao somarN    
        
          for(int i=0;i<n-1;i++){// busca n-1
        
                    printf("Digite o numero %d = ",i+1);// valores para o vetor
        
             scanf("%d",&vet);
    
        s+=vet;// soma os valores
        
    a=x;// recebe o valor da funcao somarN
    b=s;// recebe o valor da soma dos valores do vet
    t=a-b; // E finaliza  
}
    return t;