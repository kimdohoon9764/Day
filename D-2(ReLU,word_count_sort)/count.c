#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *fp=fopen("count.txt","w");

    if (fp==NULL){
        printf("파일이 존재하지않습니다.");
        return 0;
    }
    fprintf(fp,"ai ai ai python hello hello");
    printf("동작 제대로 함");
    fclose(fp);
}