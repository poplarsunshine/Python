import file as f

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    file_path = '/Users/hetao/Desktop/Code/Python/Test/File/flying_circus_cast.txt'
    file = open(file_path)
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    for line in file:
        line_str = line.strip()
        cast = line_str.split(',')[0]
        cast_list.append(cast)

    file.close()

    return cast_list

def main():
    cast_list = create_cast_list('flying_circus_cast.txt')
    for actor in cast_list:
        print(actor)

if __name__ == "__main__":
    main()

print('cast_list:' + __name__)
print('cast_list:' + f.__name__)
