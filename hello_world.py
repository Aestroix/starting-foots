'''
THERE IS ONE MASTER BRANCH

BEFORE COMMITING THERE IS A STAGING AREA 
SO WHEN YOU MAKE A CHANGE YOU CAN ADD THAT FILE TO THAT STAGING AREA

git add <file> to add file to staging area
git rm --cached <file> to unstage

To commit make sure that you configure the git using your email and username

git config --global user.email "email"
git config --global user.name "username on git"

when you commit something the commit head goes above the latest added file

git branch <branch_name>: to add a branch
git checkout <branch_name>: to change branch
git merge <branch_name>: to merge a branch to current branch

git commit -am command to do everything at once 
'''
print('hello world')

print('adding to somef branch')

print('now adding to somef branch')

'''
when you generate a pull request on the website it is working with the remote
server and you will not see any changes in the local folder in which you have 
stored the file

to find the changes in the local server use

git pull
'''