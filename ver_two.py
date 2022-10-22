import os
import argparse

parser = argparse.ArgumentParser(prog="readme.task",description="""put this program in your folder
 this is version2""")
parser.add_argument("github_name",help='your username of github')
parser.add_argument("repo_name",help='project name(repositpry name) in github')
args = parser.parse_args()



def information(repo_name):
    infor = []
    for file_adress, file_incload, exe in os.walk(os.getcwd()):
        # print(file_adress,file_incload,exe)
        if len(file_adress.split(os.getcwd() + "\\")) > 1:
            topic = file_adress.split(os.getcwd() + "\\")[-1]
        else:
            topic = repo_name
        a = [(file_adress, topic, readme_file) for readme_file in exe if ".md" in readme_file]
        infor = infor + a
    return infor


def adress_maker(github_name,repo_name):
    add = f"https://github.com/{github_name}/{repo_name}"
    return add

def link_title (topic, readme_file,  add):
   return f'# [{topic}]({add}/blob/main/{topic}/{readme_file})'

def get_question_from_file(file_adress, topic, readme_file, add):
    return_str = ""
    with open(f'{file_adress}//{readme_file}', encoding="utf-8") as readme_file:
        deta = readme_file.readlines()
        print(deta)
        for line in deta:
            if '##' in line:
                clean_line = (line.strip("#")).strip(" ")
                clean_line = " ".join(clean_line.split())#چرا با خط بالا کار نکرد؟
                spilit_clean_line = clean_line
                sighns = [char for char in clean_line if char.isalpha() == 0 and char.isnumeric() == 0 and char.isspace()==0]
                for sign in list(set(sighns)):
                    if sign == "-":
                        spilit_clean_line = spilit_clean_line.replace(sign, " ")
                    else:
                        spilit_clean_line = spilit_clean_line.replace(sign, "")
                spilit_clean_line = spilit_clean_line.lower().rstrip(" ").replace(" ","-")
                return_str = return_str + f'* [{clean_line}]({add}/blob/main/{topic}#{spilit_clean_line})'+'\n\n'
        return return_str

#print(get_question_from_file('D:\\python\\clone\\today-i-learned\\deep-learning', 'deep-learning', 'Readme.md',"lopodos"))
def joiner (repo_name, add):
    files = information(repo_name)
    links =""
    for file_adress, topic, readme_file in files:
        links += link_title(topic, readme_file,add) +"\n" + get_question_from_file(file_adress,topic, readme_file, add)
    return links

def main(github_name, repo_name):
    with open("R.md", "w+") as main_file:
        main_file.write(joiner(repo_name,adress_maker(github_name, repo_name)))
        main_file.seek(0)
        print(main_file.read())

if __name__ == '__main__':
    main(args.github_name,args.repo_name)