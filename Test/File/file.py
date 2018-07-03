import cast_list as cast

path = '/Users/hetao/Desktop/Code/Python/Test/File/my_file.txt'
f = open(path, 'w')
f.write("Hello there!\n")
f.write("Hello there!!\n")
f.write("Hello there!!!")
f.close()

camelot_lines = []

with open(path, 'r') as f:
    # file_data = f.read()
    # print(file_data)

    # print(f.read(2))
    # print(f.read(3))
    # print(f.read())

    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    for line in f:
        camelot_lines.append(line.strip())

    # print(camelot_lines)

# cast_list = cast.create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)

print(__name__)
print(cast.__name__)
