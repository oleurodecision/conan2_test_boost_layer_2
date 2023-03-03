#include <iostream>
#include "layer2Version.hh"
#include "layer2/fake.hh"

int main() {
    std::cout << Layer2_VERSION << std::endl;
	 layer2::fake();
}
