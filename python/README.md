+ Python download instructions go here

+ Python Hello World instructions go here

+ How to push up exercise 1 instructions go here

## How to create a branch for learning python

1. Change directories to your cloned github directory:
		cd ~/dev/learnTheHardWay
2. Next, create a new branch called 'learn_python_<your_name_here>'(note, get rid of the '<>' characters
		git checkout -b learn_python_<your_name_here>
+ For me this looks like 
		$git checkout -b learn_python_kevin
3. Then start coding, when you finish an exercise type the following github commands in your terminal, in order to add your code to your branch & commit the code that you've saved to your local files.:
		git add .
		git commit -m "Here's a message of what chapter I did and anything I else I want to explain for other people reading about this code"
+ For me this looks like 
		$git commit -m "Chapter 1, I installed python 3 and wrote this script to test out my new installation on my mac air"
+ Note, you can check which branch you are on and which files are 'added' for the next commit by:
		git status
	_or_
		git branch -l
+ Note, if you mess up (who messes up?) you can 'remove' files you don't want to commit changes for by using:
		git rm <file_I_made_but_do_not_want_in_github>
		git status
4. Finally, incorporate the web connection part of github, by 'pushing' your code to github.com, to the repository that you originally cloned from.
		git push origin learn_python_<name>
+ For me this looks like
		$git push origin learn_python_kevin
