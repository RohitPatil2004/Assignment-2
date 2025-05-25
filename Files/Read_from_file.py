def read_from_file(filename):
    with open(filename,'r') as file:
        content = file.read()
    print(content)

a = input("Enter file name : ")
read_from_file(a)