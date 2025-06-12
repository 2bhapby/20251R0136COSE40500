from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
from power import power
from modulo import modulo
from factorial import factorial
from root import square_root, nth_root


def main():
    print("=== Python Console Calculator ===")
    print("Available operations:")
    print("1) add      2) subtract")
    print("3) multiply 4) divide")
    print("5) power    6) modulo")
    print("7) factorial 8) square root")
    print("9) nth root")
    print("0) exit")

    while True:
        choice = input("\nSelect operation (1~9 or 0 to exit): ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                a, b = map(float, input("Enter two numbers: ").split())
                print("Result:", add(a, b))
            elif choice == "2":
                a, b = map(float, input("Enter two numbers: ").split())
                print("Result:", subtract(a, b))
            elif choice == "3":
                a, b = map(float, input("Enter two numbers: ").split())
                print("Result:", multiply(a, b))
            elif choice == "4":
                a, b = map(float, input("Enter two numbers: ").split())
                print("Result:", divide(a, b))
            elif choice == "5":
                a, b = map(float, input("Enter base and exponent: ").split())
                print("Result:", power(a, b))
            elif choice == "6":
                a, b = map(int, input("Enter two integers: ").split())
                print("Result:", modulo(a, b))
            elif choice == "7":
                n = int(input("Enter a number: "))
                print("Result:", factorial(n))
            elif choice == "8":
                n = float(input("Enter a number: "))
                print("Result:", square_root(n))
            elif choice == "9":
                n, r = map(float, input("Enter number and root degree: ").split())
                print("Result:", nth_root(n, r))
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
