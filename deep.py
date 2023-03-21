def main():
    a = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
    a = a.lower()
    match a:
        case "42":
            print("Да")
        case "сорок два":
            print("Да")
        case _:
            print("Нет")

main()