#!/usr/bin/env python3.10

def main():
    x = 0.000001
    k = 0.000001
    while x < 1:
        rez = 1 + 1 / (4 * x) + (1 * 5 * x) / (4 * 8)
        print(f"x: {x}\tf: {rez}")
        x += k


if __name__ == "__main__":
    main()
