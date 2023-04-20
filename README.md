# Precautions
Install Python
        
        https://www.python.org/downloads/ 

Setting Environment Variable.

Install Git: 

        https://git-scm.com/downloads 

Install VSCode: 
        
        https://code.visualstudio.com/ 

Create new folder on your local computer/laptop.

Right-click, Open gitbash

Open VSCode:

        Code .

SELECT INTERPRETER venv

        .venv\scripts\activate # this is from interpreter

In terminal

        python -m pip install --upgrade pip

then

        .venv\Scripts\Activate.ps1


Install pip of django


        python -m pip install django

Create new folder, example is nameyourprojectfolder

        python -m django startproject nameyourprojectfolder .

do migration

        python manage.py migrate

run your first project
    
        python manage.py runserver

In the VS Code Terminal, again with the virtual environment activated, run the development server with python manage.py runserver and open a browser to 

        http://127.0.0.1:8000/

Done, Congrats!
Furthemore, click this link:

[https://sites.google.com/view/coding9/pyhton-django](https://sites.google.com/view/coding9/pyhton-django)

# Starter-using-django
## How to push repository on github
Configure your local Git installation to use your GitHub credentials by entering the following:
fill username:

    git config --global user.name "github_username"
    
fill email:

    git config --global user.email "email_address"
    
type here:

    git config --global init.defaultBranch main

Note: Replace github_username and email_address with your GitHub credentials. 

Initial step:

    git init

#check status
    
    git status

#add all files
    
    git add .

#check the update status
    
    git status

#Ready to commit
    
    git commit -m "first commit"


#Add a new remote origin, Note: Remember, you will need to replace the highlighted parts of the username and repo name with your own username and repo name.

In git, a “remote” refers to a remote version of the same repository, which is typically on a server somewhere (in this case, GitHub). “origin” is the default name git gives to a remote server (you can have multiple remotes) so git remote add origin is instructing git to add the URL of the default remote server for this repo.


    git remote add origin git@github.com:sammy/my-new-project.git


#Ready to push
    
    git push -u origin main
    
#All together

    git init
    git add -A
    git commit -m 'Added my project'
    git remote add origin git@github.com:sammy/my-new-project.git
    git push -u -f origin main
