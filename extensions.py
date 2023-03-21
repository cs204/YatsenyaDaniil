def main():
    a = input("File name: ")
    a = a.lower()
    a = a.split(".")
    b = len(a)
    match a[b - 1]:
        case "jpg" | "jpeg":
            print ("image/jpeg")
        case "png":
            print ("image/png")
        case "pdf":
            print ("application/pdf")
        case "txt":
            print ("text/plan")
        case "zip":
            print ("application/zip")
        case "gif":
            print ("image/gif")
        case _:
            print ("application/octet-stream")

main()