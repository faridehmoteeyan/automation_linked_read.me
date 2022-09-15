import os
import argparse

# to test parsel in pycharm use configuration(up page_next to the run)
parser = argparse.ArgumentParser(prog="readme.task",description="""put this program in your folder
 we extraction question(part witch start with# in markdown filles)from dirs
 make a complite question with their link in readme.file""")
parser.add_argument("github_name",help='your username of github')
parser.add_argument("repo_name",help='project name(repositpry name) in github')
args = parser.parse_args()

def adress_maker(github_name,repo_name):
    add = f"https://github.com/{github_name}/{repo_name}"
    return add


def link_title (x,add):
   return f'# [{x}]({add}/blob/main/{x}/Readme.md)'


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


def joiner (add):
    files = [f for f in os.listdir() if os.path.isdir(f)]
    files = [f for f in files if not '.' in f]
    links =""
    for title in files:
        links += link_title(title,add) +"\n" + get_question_from_file(title,add)
    return links

def main(github_name, repo_name):
    with open("Readme.md", "w+") as main_file:
        main_file.write(joiner(adress_maker(github_name, repo_name)))
        main_file.seek(0)
        print(main_file.read())

if __name__ == '__main__':
    main(args.github_name,args.repo_name)
