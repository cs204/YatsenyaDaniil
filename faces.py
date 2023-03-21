def convert(x):
    if (":)" in x) or (":(" in x):
        x = x.replace(":)", "\N{Slightly Smiling Face}")
        x = x.replace(":(", "\N{Slightly Frowning Face}")
    return x
def main():
    x = str(input())
    x = convert(x)
    print(x)
main()