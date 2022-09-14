import os

#making dir(main_files) links
def link_title (x,add):
   return f'# [{x}]({add}/blob/main/{x}/Readme.md)'

# get question in each dir and link qustion to ther places in dir
def get_question_from_file(x,add):
    return_str = ""
    with open(f'{x}\\Readme.md', encoding="utf-8") as readme_file:
        deta = readme_file.readlines()
        for line in deta:
            if '##' in line:
                clean_line = line.strip("#").strip(" ")
                spilit_clean_line = clean_line[:-2].replace(" ", "-")
                return_str = return_str + f'[{clean_line}]({add}/blob/main/{x}#{spilit_clean_line})'+os.linesep
    return return_str

#due to we need just one arguman in write
def joiner (add):
   links =""
   for title in files:
      links += link_title(title,add) +"\n" + get_question_from_file(title,add)
      #return links
   return links

print("Instructions".center(100,"-"))
print("""put this program in your folder
 we extraction question(part witch start with# in markdown filles)from dirs
 make a complite question with their link in readme.file""")

add = input("enter your github repository address")

files_names = os.listdir()
files = [f for f in os.listdir()  if  os.path.isdir(f)]
files = [f for f in files if not '.' in f]

#make a folder and put links here
with open("Readme.md","w+") as main_file:
    main_file.write(joiner(add))
    main_file.seek(0)
    print(main_file.read())