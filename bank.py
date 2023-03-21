def main():
    a = input("Приветствие: ")
    a = a.lower()
    a = a.replace(",", "")
    a = a.split()
    if a[0] == "здравствуйте":
        print("0$")
    elif a[0].startswith("з"):
        print("$20")
    else:
        print("100$")

main()