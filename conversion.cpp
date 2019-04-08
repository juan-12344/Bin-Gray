#include <iostream>
#include<stdlib.h>
#include<conio.h>
using namespace std;
char xor_c(char a, char b) { return (a == b) ? '0' : '1'; }
char flip(char c) { return (c == '0') ? '1' : '0'; }
string binarytoGray(string binary)
{
	string gray = "";
	gray += binary[0];
	for (int i = 1; i < binary.length(); i++) {
        gray += xor_c(binary[i - 1], binary[i]);
	}

	return gray;
}

string graytoBinary(string gray)
{
	string binary = "";
	binary += gray[0];
	for (int i = 1; i < gray.length(); i++) {
		if (gray[i] == '0')
			binary += binary[i - 1];
		else
			binary += flip(binary[i - 1]);
	}
	return binary;
}
int main()
{

    int i=0;
    while(i<1000){
        cout<<"\t\t Conversiones Binario-Gray\n";
        cout<<"\t\t 1.Binario a Gray \n\t\t 2.Gray a Binario \n\t\t 3.Salir \n\n\n";
        cout<<"Elige una opcion:  ";
        int opcion;
        cin>>opcion;
        if(opcion==1){
            cout<<"\t\t Binario a Gray \n\n";
            string binary;
            cout<<"Ingresa el numero binario:  ";
            cin>>binary;
            cout<<"El numero gray es: "<<binarytoGray(binary) << endl;

        }
        if(opcion==2){
            cout<<"\t\t Gray a Binario \n\n";
            string gray;
            cout<<"Ingresa el numero gray:  ";
            cin>>gray;
            cout<<"El numero binario es: "<<graytoBinary(gray) << endl;

        }
        if(opcion==3){
            cout<<"Hasta pronto";
            break;
        }
        getch();
        system("cls");
        i++;
    }



}
