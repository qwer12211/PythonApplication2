import math

while True:
    print("�������� ��������:")
    print("1. ��������")
    print("2. ���������")
    print("3. ���������")
    print("4. �������")
    print("5. ���������� � �������")
    print("6. ���������� ������")
    print("7. ���������")
    print("8. �����")
    print("9. �������")
    print("10. �������")
    print("11. �����")

    operation = input("������� ����� ��������: ")

    if operation == '11':
        print("�����.")
        break

    if operation in ('1', '2', '3', '4', '5'):
        a = float(input("������� ������ �����: "))
        b = float(input("������� ������ �����: "))

        if operation == '1':
            result = a + b
        elif operation == '2':
            result = a - b
        elif operation == '3':
            result = a * b
        elif operation == '4':
            if b == 0:
                print("������� �� 0 ����������.")
                continue
            result = a / b
        elif operation == '5':
            result = a ** b

    elif operation in ('6', '7', '8', '9', '10'):
        c = float(input("������� �����: "))

        if operation == '6':
            if c < 0:
                print("���������� ������ �������������� ����� �� ����� ����.")
                continue
            result = math.sqrt(c)
        elif operation == '7':
            if c < 0:
                print("��������� �������������� ����� �� ����� ����.")
                continue
            result = math.factorial(int(c))
        elif operation == '8':
            result = math.sin(c)
        elif operation == '9':
            result = math.cos(c)
        elif operation == '10':
            result = math.tan(c)

    else:
        print("����������� ����� ��������.")
        continue

    print(f"���������: {result}")
    