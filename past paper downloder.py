from pymsgbox import alert
from bs4 import BeautifulSoup as bs
import requests
import argparse
import os
from termcolor import cprint
import datetime
from pygame import mixer

mixer.init()
notifier_dir = r"Alka Yagnik - Agar Tum Saath Ho.mp3"
mixer.music.load(notifier_dir)
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--subject', required=True, type=str, action='store')
parser.add_argument('-y', '--year', required=True, action='store', help="Select a year.")
parser.add_argument('-pt', '--paper_type', required=False, type=str, action='store', help="Leave empty to download all")

args = parser.parse_args()
if args.year.isdigit():
    years = [args.year]
else:
    year_range = args.year.strip().split("-")
    years = list(range(int(year_range[0]),int(year_range[1])+1))

if args.paper_type:
    if "," in args.paper_type:
        args.paper_type = args.paper_type.split(",")
    else:
        args.paper_type = [args.paper_type]

if "," in args.subject:
    args.subject = args.subject.split(",")
elif "*" in args.subject:
    args.subject = ["Physics", "Chemistry", "Computer" , "English", "Maths", "EGP"]
else:
    args.subject = [args.subject]
    
#print(years)


def makedir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError as err:
        pass


def download(down_path, filename):
    try:
        os.mkdir(down_path)
    except FileExistsError as err:
        pass

    if not os.path.isfile(f'{down_path}/{filename}'):
        with open(f'{down_path}/{filename}', 'wb') as f:
            f.write(requests.get(file_link).content)
    cprint(f"Downloaded {filename}", 'green')

    return True

time_start_total = datetime.datetime.now()
download_files_total = 0
for subject in args.subject:
    for year in years:
        cprint(f"{subject:^29}","cyan")
        cprint(f"{year:^29}","cyan")
        subjects = {
            "Physics": "Physics (9702)",
            "Chemistry": "Chemistry (9701)",
            "Computer": "Computer Science (for first examination in 2021) (9618)" if int(year)>=2021 else "Computer Science (for final examination in 2021) (9608)",
            "English": "English - Language AS and A Level  (9093)",
            "Maths": "Mathematics (9709)",
            "Biology": "Biology (9700)",
            "EGP": "English General Paper (AS Level only) (8021)",
            "F.Maths":"Mathematics - Further (9231)",
        }


        url = f"https://papers.gceguide.com/A%20Levels/{subjects[subject]}/{year}"

        try:
            r = requests.get(url)
        except:
            cprint("No Internet Connection","red")
            exit(1)
        soup = bs(r.text, 'html.parser')

        files = soup.select('li.file')

        # Might be a bad practice to do it this way but here it goes.
        user_path = os.path.expanduser('~/Documents')
        makedir(f'{user_path}/PastPapers')
        makedir(f'{user_path}/PastPapers/{subject}')
        makedir(f'{user_path}/PastPapers/{subject}/{year}')

        time_start = datetime.datetime.now()
        #cprint("FOUND" if files else "EMPTY","red" if not files else "green",sep="\n")
        download_files = 0
        for file in files:

            link = file.find_all('a', href=True)[0]
            file_link = f"{url}/{link['href']}"
            
            file_type = link['href'].split("_")[2]
            
            if ".pdf" in file_type:
                file_type = file_type.strip(".pdf")
            if args.paper_type == '' or not args.paper_type:
                try:
                    int(file_type)
                    file_type = link['href'][-6:-4]
                except ValueError as err:
                    pass
                path = f'{user_path}/PastPapers/{subject}/{year}/{file_type}'
                makedir(path)
                download(path, link['href'])
                download_files += 1

            elif file_type in args.paper_type:
                path = f'{user_path}/PastPapers/{subject}/{year}/{file_type}'
                makedir(path)
                download(path, link['href'])
                download_files += 1

        time_finish = datetime.datetime.now()
        #os.system("clear")
        cprint("-----------------------\n Details:\n----------------------- ", 'magenta')
        cprint(f"Start time:","cyan",end=' ')
        cprint(f"{time_start:%Y-%m-%d %I:%M:%S}","yellow")
        cprint(f"Finished time:","cyan",end=' ')
        cprint(f"{time_finish:%Y-%m-%d %I:%M:%S}", 'yellow')
        cprint(f"Total Time Taken:","cyan",end=' ')
        cprint(f"{time_finish - time_start!s}", 'yellow')
        cprint(f"Total Downloads:","cyan",end=' ')
        cprint(f"{download_files} files.", 'yellow')
        mixer.music.play()
        alert(text=f"{subject} {year}'s Past Paper Downloaded!",title="COMPLETED",button="Done",timeout=6000)
        mixer.music.pause()
        download_files_total += download_files
        if subject != args.subject[-1] or year != years[-1]:
            os.system("clear" if not os.name=="nt" else "cls")
            
time_finish_total = datetime.datetime.now()
print()
cprint("-----------------------\n Overall Details:\n----------------------- ", 'magenta')
cprint(f"Start time:","cyan",end=' ')
cprint(f"{time_start_total:%Y-%m-%d %I:%M:%S}","yellow")
cprint(f"Finished time:","cyan",end=' ')
cprint(f"{time_finish_total:%Y-%m-%d %I:%M:%S}", 'yellow')
cprint(f"Total Time Taken:","cyan",end=' ')
cprint(f"{time_finish_total - time_start_total!s}", 'yellow')
cprint(f"Total Downloads:","cyan",end=' ')
cprint(f"{download_files_total} files.", 'yellow')
alert(text=f"{' and '.join(args.subject)} ({', '.join(map(str,years))})'s Past Paper Downloaded!",title="COMPLETED ALL DOWNLOADS",button="Done", timeout=60000)
