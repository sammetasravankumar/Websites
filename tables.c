#include<stdio.h>
int main()
{
int a,i;
printf("enter the number to form that table:");
scanf("%d",&a);
printf("the following is a table of:\n",a);
for(i=1;i<=10;i++)
{
printf("%d*%d=%d\n",a,i,a*i);
}
return 0;
} 