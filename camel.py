fraza = str(input("Верблюжий стиль: "))
snake = list()
for w in fraza:
    if w == w.upper():
        snake.append("_")
        snake.append(w.lower())
    else:
        snake.append(w)
if (snake[0] == "_"):
    snake.remove("_")
print("".join(snake))