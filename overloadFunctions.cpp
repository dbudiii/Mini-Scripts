//Calculate area of circle using a function

//Need to include <cmath> and define _USE_MATH_DEFINES so that we can use M_PI, which is the constant for pi 
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>


//calculate area of circle 
double area(double r) {
	double pi = M_PI; 
	
	double result = pi * r * r;

	return result;
}

//calculate area of rectangle 
int area(int length, int width) {
	return length * width;
}

//calculate area of triangle
double area(double a, double b, double c) {
	double s = (a + b + c) / 2;
	double area = std::sqrt(s * (s - a) * (s - b) * (s - c));
	
	return area;
}

//calculate area of square
int area(int side) {
	return side * side;
}


int main() {
	
	double radius = 5.0;
	double a = 3.0, b = 4.0, c = 5.0;
	int length = 5, width = 3;
	int side = 4;

	std::cout << "The area of Circle is: " << area(radius) << "\n";
	std::cout << "The area of rectangle is: " << area(length, width) << "\n";
	std::cout << "The area of triangle is: " << area(a, b, c) << "\n";
	std::cout << "The area of square is: " << area(side) << "\n";

	
	return 0;
}
