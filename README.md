# Machine_learning_project

### Software and account requirement

1. [Git CLI](https://git-scm.com/download/win)


#### TO clone git hub repository in VS and local system

by commands from powershell/command prompt
1.  create new repository in github
2.  #command - git clone "Repository Link"
3.  #comand - ls or dir # to check directory
4.  #comand - cd "to change directory paste directory location"
5.  #comand - code .


#### 2nd way to clone and create repoaitory in local system

1. create new repository in github
2. create fresh folder in any location of Local system
3. click in folder and press shift+ right click and power shell/command prompt
4. in power shell write # comand  -  git clone "Repository Link"
4. #command - pwd
5. open VScode and select that project fold and in that that clone repository 

6. in Vscode open terminal and then select gitbash terminal 



#### Creating Conda evironment - Commands



command promt/dit bash/powershell

````
conda --version
````
````
conda create -p venv python== 3.7 -y  " Create venv in tha same directory"
````
````
conda activate venv/
````
Or
````
conda activate venv
````

"to install requirements file"
````
pip install -r requirements.txt

````

> Note : create app.py file and in command prompt type 
````
python app.py
````


#### Push changes to github # comands

> note: to Add files in git 

````
git add filename "to maintain the version control system"
````
OR
````
git add "file1,file2....filen"
````
OR
````
git add . "to add all the files in one line"
````
git status 
````
 > Note : "suppose you have create a file but it not added in git , this command will provide status of which file is not tracked by git"
````

````
git commit  "to comit change"
````

to check log
````
git log
````

> Note: to commit changes

````
git commit -m "message"
````

> Note: To push changes/to send version

````
git push origin main
````
To check remote URL

````
git remote -v
````
to know branch
````
git branch
````
