def get_points():
    while True:
        print('Please enter a rating from 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Please enter 1 to 5')
                point = input()
            else:
                print('Please enter a comment')
                comment = input()
                post = f'Points: {point} Comments: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
        else:
            print('Please enter the evaluation points as numbers')


def check_results():
    print('Results so far')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()


while True:
    print('Please select the process you wish to perform')
    print('1: Enter evaluation points and comments')
    print('2: Review the results so far')
    print('3: Exit')
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            get_points()
        elif num == 2:
            check_results()
        elif num == 3:
            print('Exit')
            break
        else:
            print('Please enter 1 to 3')
    else:
        print('Please enter 1 to 3')
