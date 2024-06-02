//Display a set of values in array 

#include <iostream>

using namespace std; 

int main() {

	int a[10];

	//Input values into array
	for (int i = 0; i < 10; i++) {

		cout << "Enter the value for a[" << i << "]. \n";
		cin >> a[i];
	}

	//Display the values in the array
	for (int i = 0; i < 10; i++) {

		cout << "Value in a[" << i << "] is: " << a[i] << "\n";


	}


	return 0; 
}
