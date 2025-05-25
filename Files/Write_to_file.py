def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}.")

a = input("Enter File name : ")
b = input("Enter content : ")
write_to_file(a,b)
