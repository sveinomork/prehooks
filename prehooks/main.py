# my_python_project/main.py


def add(a, b):
    return a + b  # Introduced a bug: should be addition, but subtraction is used


if __name__ == "__main__":
    result = add(2, 3)
    print(f"The result is {result}")
