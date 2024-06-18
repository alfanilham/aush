
import os

# colors
x  = '\033[0m'  # reset
gr = '\033[90m' # grey
lr = '\033[91m' # light red
lg = '\033[92m' # light green
ly = '\033[93m' # light yellow
mg = '\033[95m' # magenta
cy = '\033[96m' # cyan
w  = '\033[97m' # white

def banner():
    print(f"""
{lr}               __                         __                _ __ 
  ____ ___  __/ /_____  ____  __  _______/ /_        ____ _(_) /_
 / __ `/ / / / __/ __ \/ __ \/ / / / ___/ __ \______/ __ `/ / __/
/ /_/ / /_/ / /_/ /_/ / /_/ / /_/ (__  ) / / /_____/ /_/ / / /_  
\__,_/\__,_/\__/\____/ .___/\__,_/____/_/ /_/      \__, /_/\__/  
                    /_/                           /____/         {x}

Authored by : smartfhand
Github      : @alfanilham

""")

def push():
    
    banner()
    os.system("git add .")
    commit_name = input("Commit Name: ")
    print("\nCommit Proccessing . . .\n")
    os.system(f"git commit -m '{commit_name}'")
    os.system("git push")
    print(f"""
{ly}Successfully push for commit {commit_name}!!{x}""")

if __name__=="__main__":
    try:
        push()
    except KeyboardInterrupt:
        ngecrot = input("\n\nLo mo kluar? y(Yes)/n(No): ")
        if ngecrot == "y":
            exit("\nTolol kamu ya.")
        else:
            exit("\nBodoamat anjg.")
