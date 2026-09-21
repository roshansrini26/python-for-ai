# Git and Github

Git is a powerful tool that constantly keeps track of every change you make to your files. Keeps different versions of code

## Difference between Git and Github

Git runs locally on your host and keeps track of the changes and organized.
Github is central hub that merges and acts as the central online server 

## Architecture
Local and remote

**Local**
- Working directory (write, create, edit)
- Staging - save changes
- Local repository: Temporary area where files sit between working directory and repository area
- Commit 
- Push

**Repository** is a place where all the versions of your files and their complete change history are stored

**Remote**

- Access from anywhere (Cloud backup for code)

Store code to remote
Pull code to local


## Git commands

### To initialise Git in the working directory to track 
```python
git init
ls -la #To show hidden files
```
**.git** folder - keeps all internal data

### Clone remote repo
```python
git clone ____
```
### Git to see modified files
```python
git status
```
### Staging
```python
git add --all #or 
git add -A
git reset #remove the staging files back to the local
```
Stage every single change across the entire project

```python
git add .  #Stage the cha ges within the current directory youre in
git add * #Only stages new or modified files doesnt keep track of deleted file
git add folder/filename #To stage only specific file
git add *.txt #stages all specific extention files
```
Staging area where we can review, adjust, remove changes

### Commit
```python
git commit -m "message" #-m is short message
```

### Identity authorization
```python
git config --global user.email "ur_email"
git config --global user.name "ur_name"
```
--local git for particular file

```python
git reset HEAD #rollback to the previous commit, undo last commit
git reset --hard #brings back the deleted files and changes
```

### delete and stage 
```python
git add .
git rm filename
git rm -f filename #file is forcefully deleted rather modification and unstaged
git rm --cached filename #removes from staging area but keeps it locally
git rm -r <folder> #-r for recursive
```

### view commits
```python
git log #commit history
git log --oneline #short commit history
```

## Branching
main - default branch
create sepearate developement branch to test newly developed features and commit and merge to commit
**Merge** combining the chages from two branch into one
Whenever we create a new branch it inherits the current branch

```python
git branch #to show list of branches
git branch branchname #create branch
git checkout branchname #to move to branch
```

- both the branches are at their commit stage, then move to the branch and merge
```python
git merge main -m "message"
```
**Merge conflict** arrives when same part of the same file changed differently in branches

## Switching back branches

```python
git log --oneline
git checkout commit-id #before doing this the exisitng branch should be staged and commited
git diff commit_id_1 commit_id_2 #show changes bewtween commits

```
to exit from log files press **q**

## Remote repository

- **PUSH**: Sending local changes to the remote
- **FETCH**: Bringing remote changes into your local repository, but not merging them yet
- **PULL**: Fetching plus merging-so your working directory immediately reflects the remote changes
PULL = FETCH + MERGE

```python
git push origin main #orgin refers to remote repo and main is the branch
git fetch #brings changes from remote repo but dont get appeared in your local file system
git merge #changes appear in my local files
git pull #performs both fetch and merge
```

When changes are taken place over a large files and reverting back
```python
git restore #undo local uncommited changes
git restore .
git restore --staged fileName #restore a staged file
git restore --staged .
```

Temporarily set aside unfinished work, switch another branch to do something
git doesnot allow to switch branchs before commit or stash
git can store multiple stashes 
```python
git stash
git stash pop #bring back the stash
git stash list
git stash apply stash@{0} #stash specific 
git stash drop #drop the stash
```
```python
git stash pop #stash is removed completely from the stash list and applied
git stash apply #stash is applied and also stays in the stash list
```
Revert - used to undo the changes made in a previous commit, but instead of deleting that old commit, it creates a new one that reverses those changes
```python
git revert commit_id
:wq
```
git reset and git revert -> reset deletes all previous commits, revert creates new commit instead of deleting

**Rebase**: refelect changes carried out in another branch while working on the same branch

```python
git rebase branchName
```
**Pull request**: asking permission to merge your code base into the main

