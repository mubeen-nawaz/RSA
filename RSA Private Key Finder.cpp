// Coding with Mubeen Nawaz.
// C++ Program to find Private Key in RSA.
// When n < 1000000.
#include <iostream>
using namespace std;
int main(){
	float n, e, p, q, a, d, d2;
	int	d1, i = 0;
	cout<<"Enter p: ";
	cin>>p;
	cout<<"Enter q: ";
	cin>>q;
	cout<<"Enter Public Key: ";
	cin>>e;
	n = p * q;
	a = (p-1)*(q-1);
	cout<<"\n*************************\n";
	do{
		d = (1 + a * i) / e;
		cout<<"\n"<<d<<"\n";
		d1 = d;
		d2 = d - d1;
		i++;
	}while(d2 != 0);
	cout<<"\n*************************\n"
	    <<"\nn is: "<<n<<"\n"
		<<"\nPhy(n) is: "<<a<<"\n"
	    <<"\nPrivate Key is: "<<d<<"\n";
	return 0;
}