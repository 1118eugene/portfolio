// C++
#include <iostream>
#include <cmath>

float calculateCircleArea(float radius) {
    return M_PI * pow(radius, 2);
}

float calculateTriangleArea(float base, float height) {
    return 0.5 * base * height;
}

float calculateRectangleArea(float length, float width) {
    return length * width;
}

int main() {
