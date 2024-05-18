//Calculate area of circle using a function

//Need to include <cmath> and define _USE_MATH_DEFINES so that we can use M_PI, which is the constant for pi 
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>



double circleArea(double r) {
	double pi = M_PI; 
	
	double result = pi * r * r;

	return result;
}


int main() {
	
	double radius; 
	std::cout << "Enter radius: \n";
	std::cin >> radius; 

	std::cout << "The radius is: " << circleArea(radius);
	
	return 0;
}
