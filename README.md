# Intermediate Github Workshop

Learn all about branches, merging, rebasing and more - hosted by CCIS Fellows!

This repo contains a simple `fib.py` file which contains a simple implementation of the fibonnaci sequence in Python. In addition there are the following branches:

- `fast_fib`
  - A faster implementation of the fibonnaci sequence
- `ask_for_input`
  - Allow the user to enter input
  - **Note:** only works in Python3
- `alphabet`
  - Adds a new text file with some letters of the alphabet
- `alphabet_conflict`
  - Also adds a text file with some letters of the alphabet

The point of these branches is to give you a chance to practice merging/rebasing them into master! Merging `alphabet` into master and then merging `alphabet_conflict` will cause a merge conflict, try to resolve it!

Example usage:

```
$> git clone https://github.com/Derrreks/Fall2019IntermediateGithubWorkshop.git
$> cd Fall2019IntermediateGithubWorkshop
$> git branch
  alphabet
  alphabet_conflict
  ask_for_input
  fast_fib
* master
$> git merge fast_fib            <-- this will merge fast_fib into master!
$> git merge alphabet            <-- this will merge alphabet into master, you should see a new file!
$> git merge alphabet_conflict
Auto-merging abc.txt
CONFLICT (add/add): Merge conflict in abc.txt
Automatic merge failed; fix conflicts and then commit the result.
$>
$> ... figure out how to resolve the conflict! ...
$>
```
