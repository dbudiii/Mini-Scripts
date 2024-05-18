#include <iostream>

//Program to calculate sum of numbers from m to n.


//calculating the sum 
int calculate(int a, int b) {
	
	int sum = a;
	for (int i = 0; i <= ((b+1) - a); i++) {
		a += 1; 
		sum += a; 
	}

	return sum;
}

int main() {

	//declaring variables
	int a; 
	int b; 

	//asking for first number
	std::cout << "Enter first number: \n";
	std::cin >> a; 

	//asking for second number 
	std::cout << "Enter second number: \n";
	std::cin >> b;

	//ensuring that b is the larger number 
	if (a > b) {
		int temp = a;
		a = b;
		b = temp;
	}

	//calculating the sum 
	int result = calculate(a, b); 
	std::cout << result;

	return 0; 
}
