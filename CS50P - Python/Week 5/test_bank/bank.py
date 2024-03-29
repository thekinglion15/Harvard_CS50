def main():
    answer = input("Greeting: ").lower().strip()
    print(f"${value(answer)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()