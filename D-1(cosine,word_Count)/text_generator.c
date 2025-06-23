#include<stdio.h>
#include<stdlib.h>



int main(){
    FILE *fp=fopen("test.txt","w");
    if (fp==NULL){
        printf("파일을 찾을 수 없습니다.");
    }
    else{
        fprintf(fp,"ai ai python world hello ai");
    }
    fclose(fp);
    return 0;
}