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
