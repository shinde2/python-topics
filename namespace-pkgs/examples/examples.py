from math_namespace.addition import Compute as Add
from math_namespace.multiplication import Compute as Mul

def main():
    add = Add(2, 5)
    mul = Mul(2, 5)

    print(f"2 + 5 is {add.get()}")
    print(f"2 * 5 is {mul.get()}")

if __name__ == "__main__":
    main()