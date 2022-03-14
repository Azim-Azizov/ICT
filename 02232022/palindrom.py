from math import factorial


def choose_option():
    option = input("1 - Polindrom\n2 - Chess table\n3 - Beautiful numbers\n4 - Factorial sum checker\n5 - threedigitnumbers\n0 - Quit app\n\nChoose option:")
    if option == "0":
        quit()
    return_option(option)

def return_option(option):
    if option == "1":
        string = input("polindrom role checking.Type 0 to go back.\n\nType a string: ")
        if string == "0":
            choose_option()
        if string == string[::-1]:
            print("is palindrom")
        else:
            print("is not polindrom")
    if option == "2":
        try:
            letter, number = input("Chess table\nType 0 to go back\n\nType a chess coordinates (use only upper case and separate by ', '): ").split(", ")
        except:
            choose_option()
        try:
            if (letter in "ACEG" and number in "1357") or (letter in "BDFH" and number in "2468"):
                print("Black")
            elif (letter in "ACEG" and number in "2468") or (letter in "BDFH" and number in "1357"):
                print("White")
            else:
                print("Incorrect")
        except:
            print("Incorrect")
    if option == "3":
        try:
            range1, range2 = map(int, input("Beautiful numbers.\nType 0 to go back.\n\nEnter two numbers separated by ', ': ").split(", "))
        except:
            choose_option()
        numbers =  list(range(range1, range2 + 1))
        results = ""
        for i in numbers:
            sums = 0
            for b in str(i)[:-1]:
                sums += int(b)
            if sums == i % 10:
                results += f"{i}\n"
        print(results)
    if option == "4":
        try:
            range1, range2 = map(int, input("Factorial sum checker.\nType 0 to go back.\n\nEnter two numbers separated by ', ': ").split(", "))
        except:
            choose_option()
        numbers =  list(range(range1, range2 + 1))
        results = ""
        for i in numbers:
            sums = 0
            for b in str(i):
                sums += factorial(int(b))
            if sums == i:
                results += f"{i}\n"
        print(results)
    if option == "5":
        results = []
        for i in range(100, 1000):
            results += [int(i / 100 + i / 10 % 10 + i % 10)]
        n = len(results)
        for c in range(n -  1):
            if results[c] > results[c + 1]:
                results[c], results[c + 1] = results[c + 1], results[c]
        print(results)
    choose_option()

choose_option()
