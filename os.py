import os
# print(os.uname())
# print(os.path.abspath('../'))
# os.rmdir('./abc')
import shutil

# shutil.rmtree('./abc', ignore_errors=True)
# os.mkdir('hello/as/sd')
# os.makedirs('hello/as/sd')
# shutil.copytree("newpos", "newpos2")
shutil.rmtree("newpos")
shutil.move("newpos2/as", "newpos")
