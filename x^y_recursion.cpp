//Calculate x^y using recursion

#include <iostream>
#include <math.h>


long long power(long long x, long long y) {

	if (y == 0) {
		return 1; 
	}
	else {
		return x * power(x, y - 1); 
	}

}


int main() {

	std::cout << "Enter the numbers for x^y: \n";
	int x, y; 
	std::cin >> x >> y; 
	std::cout << "The result is: " << power(x, y);
	return 0;
}
