def main():
    a, b, c = map(float, input("Nhập ba số a, b, c: ").split())
    max_value, min_value = max(a, b, c), min(a, b, c)
    print(f"Giá trị lớn nhất là : {max_value}\nGiá trị nhỏ nhất là : {min_value}")

if __name__ == "__main__":
    main()

