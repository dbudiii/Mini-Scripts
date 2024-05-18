#include <iostream>

//Program to print stars Sequence1.

int main() {


	//runs the amount of rows we need
	for (int i = 1; i <= 5; i++) {

		//runs the amount of stars we need, which equals what row it is 
		//j set to i doesn't work the condition immediately starts at the upper limit, so it only iterates once
		for (int j = 1; j <= i; j++) {
			std::cout << "*";

		}
		std::cout << "\n";
	}

	return 0; 
}
