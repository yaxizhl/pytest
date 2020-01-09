with open('./file.txt', 'a') as f:
    f.write('\n你好')
with open('./file.txt') as f:
    print(f.read())
