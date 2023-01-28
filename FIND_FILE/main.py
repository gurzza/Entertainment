import os
import find_path
import pathlib

flag = True
file_name = ''
path = 'D:\\'

while flag:
    print('Enter file name with extension (like *.jpg, *.txt): ', end='')
    file_name = input().strip()
    if pathlib.Path(file_name).suffix == '':
        print('ERROR! Enter file name one more time')
        continue

    while True:
        print('Enter search depth > 0: ', end='')
        depth = int(input())
        if depth > 0:
            break
        print('INCORRECT DEPTH! Try one more time')

    status = False
    op = find_path.find_file(file_name, path, depth)
    if op:
        print('Full path: ' + op)
    else:
        print('Nothing found')

    ans = ''
    while ans not in ['yes', 'no']:
        print('Do you want to find anything else? (yes/no) ', end='')
        ans = input().strip().lower()

    match ans:
        case 'yes':
            flag = True
        case 'no':
            print('Bye')
            flag = False
