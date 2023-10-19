#include<iostream>
using namespace std;

int main(){
	int num,n,rev = 0,digit;
	cout<<"Enter a Number : ";
	cin>>num;
	n = num;
	do{
		digit = num % 10;
		rev = (rev * 10) + digit;
		num = num / 10;
	}while(num != 0);
	if(n == rev){
		cout<<n<<" is palindrome number.";
	}
	else{
		cout<<n<<" is not palindrome number.";
	}
	return 0;
	
}
