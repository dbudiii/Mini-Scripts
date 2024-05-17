#include <iostream>
#include <cctype>

double convertF(double a) {
	return a*(9.0/5.0)+32;
}

double convertC(double  a) {
	return (a - 32) * (5.0 / 9.0);
}

int main()
{
	std::cout << "Which unit do you have? Select C/F\n";
	char unit;
	std::cin >> unit;
	unit = static_cast<char>(std::tolower(unit));

	std::cout << "Enter number to convert!\n";
	double a;
	std::cin >> a;

	//Checking if user has celsius wants to convert to fahrenheit
	if (unit == 'c') {
		std::cout << convertF(a);
	}
	//Checking if user has fahrenheit wants to convert to celsius
	else if (unit == 'f') {
		std::cout << convertC(a);
	}
	else {
		std::cout << "Error, select C/F";
	}

	return 0;
}
