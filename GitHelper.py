import os 
import sys

def print_goodbye_message():
    print("Thank You for Using Githelper!!!")
    sys.exit()

def take_valid_input(msg,values_permissible):
    
    while(1):
        ip=input(msg).lower()

        if(ip in values_permissible):
            break
        
    return ip

def add_file_by_file():

    while(1):
        file_name=input("Enter The File Name:")

        if(file_name==''):
            break
        else:
            os.system(f'git add {file_name} -f')



if __name__=='__main__':

    # Taking the user email and name for Auth
    user_email=input("Please Enter Your Email with which your Github Account is linked:")
    user_name=input("Please Enter Your UserName of your Github Account:")

    
    # Git Auth
    os.system(f'git config --global user.name "{user_name}"')
    os.system(f'git config --global user.email "{user_email}"')
    

    # Initialising Empty git Repo in the Directory
    os.system('git init')

    # Create README.md if not created
    try:
        with open('README.md','r') as fp:
            pass
    except:
        with open('README.md','w') as fp:
            pass
    
    # Reading the Contents of .gitignore if present and if not Creating one file of that kind
    try:
        with open('.gitignore','r') as fp:
            pass

    except:
        with open('.gitignore','w') as fp:
            pass


    '''git add command'''
    
    # Taking the User Input
    type_of_adding=take_valid_input("Press 'yes' to add all the files or press 'no' to add the files manually:",['y','n','yes','no'])

    if(type_of_adding=='y' or type_of_adding=='yes'):
        os.system('git add .')
    
    else:
        add_file_by_file()

    
    # Taking the commit message
    
    commit_msg=input("Enter the Commit Message:")
    commit_desc=input("Enter the Commit Description:")

    os.system(f'git commit -m "{commit_msg}" -m "{commit_desc}"')

    # Taking the User input about his/her wish to push the files in a Remote Repo or not
    remote_or_not=take_valid_input("Press 'yes' to add a Remote Origin or press 'no' to exit the process:",['y','yes','n','no'])

    # If the user does not want to add to Remote Repo,The Helper Terminates
    if(remote_or_not=='n' or remote_or_not=='no'):
        print_goodbye_message()

    
    # Adding a remote origin(If Already present then overwriting it) and Branch Name
    repo_url=input("Please Enter the URL of the Repo:")
    result=os.system(f'git remote add origin {repo_url}')
    if(result!=0):
        os.system(f'git remote set-url origin {repo_url}')


    
    branch_name=input("Please Enter the Branch name of Your Repo in which You want these files to push in(Leave it blank for 'master' Branch):")

    if(branch_name==''):
        branch_name='master'

    if(branch_name!='master'):
        os.system(f'git branch {branch_name}')

    
    os.system(f'git push origin {branch_name}')
    print_goodbye_message()
