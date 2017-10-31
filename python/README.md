## Advanced Instructions:
  + I want to take the use of the terminal up just one notch during these exercises.

  * In addition to publishing ex0.py, ex1.py etc.. I want you to 'pipe' the final output for each exercise into the folder solution/ex#.txt.  For example:
      * Finishing Exercise 1 will consist of:
          1. ex1.py
          2. solutions/ex1.txt
      * Where ex1.py is the python code from the book and solutions/ex1.txt is the output that your python script gave to the terminal when you ran it. 

  * Why?
      * I believe using the terminal for something as silly as this right up front, will get you that much more used to using it for simple task like this.  It will also make 'piping' a familiar concept and can become a powerful tool to use later on.



## How to create a branch for learning python & contributing to this Repository

1. Change directories to your cloned github directory:

```bash
    cd ~/dev/learnTheHardWay
```

2. Next, create a new branch called 'learn_python_<your_name_here>'(note, get rid of the '<>' characters

```bash
    git checkout -b learn_python_<your_name_here>
```
+ For me this looks like 

```bash
    $git checkout -b learn_python_kevin
```
3. Then start coding, when you finish an exercise type the following github commands in your terminal, in order to add your code to your branch & commit the code that you've saved to your local files.:

```bash
    git add .
    git commit -m "Here's a message of what chapter I did and anything I else I want to explain for other people reading about this code"
```
+ For me this looks like 

```bash
    $git commit -m "Chapter 1, I installed python 3 and wrote this script to test out my new installation on my mac air"
```
  + Note, you can check which branch you are on and which files are 'added' for the next commit by:

```bash
    git status
```
_or_
```bash
    git branch -l
```
+ Note, if you mess up (who messes up?) you can 'remove' files you don't want to commit changes for by using:
    
```bash
    git rm <file_I_made_but_do_not_want_in_github>
    git status
```

4. Finally, incorporate the web connection part of github, by 'pushing' your code to github.com, to the repository that you originally cloned from.

```bash
git push origin learn_python_<name>
```
+ For me this looks like

```bash    
    $git push origin learn_python_kevin
```
