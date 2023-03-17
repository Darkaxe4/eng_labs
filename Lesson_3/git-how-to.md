1. Generate ssh key with $ ssh-keygen -t ed25519 -C "your_email@example.com"
1. Add the key to the ssh-agent $ ssh-add ~/.ssh/id_ed25519
1. Add the .pub key to the gitHub
1. Run $ git config --global user.mail "your_email@example.com"
1. Run $ git config --global user.name "your_name"
1. Run $ git init
1. Do what you want

List of most used commands:
* git commit -m "some description" - to make a commit
* git clone - to clone some repo from GH
* git pull - to get newest version of repo
* git push - to send commits to server
* git branch - to create a new branch
* git checkout "_name_" - to change current branch to one with name "_name_"
* git status - to get status of repo
* git fetch - to get updates in the all branches
* git log - to get history of repo
