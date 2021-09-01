#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

float f(float x){
    float y = pow(x,3) - 9*x+3;
    return y;
}

float bissecao(float a, float b, float error){
    float med, fa,fb,fmed;
    fa=f(a);
    fb=f(b);
    while(fabs(b-a)>error){
        med = (a+b)/2;
        fmed=f(med);
        if(fa*fmed < 0){
            b = med;
            fb = fmed;
        }

        else{
            a = med;
            fa = fmed;
        }
    }

    med = (a+b)/2;
    return med;
}

int main(void) {
    setlocale(LC_ALL, "Portuguese_Brasil");
    float a,b,med,error;
    printf("Metodo da Bisseção\n");
    printf("Error: ");
    scanf("%f", &error);
    
    printf("A: ");
    scanf("%f", &a);
    printf("B: ");
    scanf("%f", &b);
    
    if(f(a)*f(b) > 0){
        printf("Erro : O intervalo não está aqui\n");
        printf("Digite um novo intervalo !\n");
        
    }

    else {
        med = bissecao(a,b,error);
        printf("Raiz aproximada = %0.4f", med);
    }
}