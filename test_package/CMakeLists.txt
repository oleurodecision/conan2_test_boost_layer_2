cmake_minimum_required(VERSION 3.19)
project(PackageTest CXX)

find_package(layer2 REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example layer2::layer2)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
