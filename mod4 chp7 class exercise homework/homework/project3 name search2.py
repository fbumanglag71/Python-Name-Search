def main():
    girls_names = []
    boys_names = []

    # Read girls' names from file
    girls_file = open('girlsname.txt', 'r')
    girls_names = girls_file.read().splitlines()
    girls_file.close()

    # Read boys' names from file
    boys_file = open('boysname.txt', 'r')
    boys_names = boys_file.read().splitlines()
    boys_file.close()

    boy_name = input("Enter a boy's name: ")
    girl_name = input("Enter a girl's name: ")

    if boy_name and girl_name:
        if boy_name in boys_names and girl_name in girls_names:
            print(f"Both {boy_name} and {girl_name} are among the most popular names.")
        elif boy_name in boys_names:
            print(f"{boy_name} is among the most popular boy's names, but {girl_name} is not among the most popular girl's names.")
        elif girl_name in girls_names:
            print(f"{girl_name} is among the most popular girl's names, but {boy_name} is not among the most popular boy's names.")
        else:
            print(f"Neither {boy_name} nor {girl_name} are among the most popular names.")
    elif boy_name:
        if boy_name in boys_names:
            print(f"{boy_name} is among the most popular boy's names.")
        else:
            print(f"{boy_name} is not among the most popular boy's names.")
    elif girl_name:
        if girl_name in girls_names:
            print(f"{girl_name} is among the most popular girl's names.")
        else:
            print(f"{girl_name} is not among the most popular girl's names.")
    else:
        print("No names entered.")

# Run the main function
main()





