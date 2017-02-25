h1 Diffstring
=========
Diffstrings is a script for compare a bunch of files and show diffs between all of them (it literally reads every file and chops same amount of same strings in all objects of files it had read). Try it to _get_ _my_ _number_.

*Usage*:
./diffstrings.py file1 file2 [file3...]

*Requirements*
* Python3
* colored

*Example*
![usage example](/diffstrings.py?raw=true)

*NB*
It requires pretty much RAM if you are checking big files (every file will be read and hold in RAM). I need it for comprasion of very tiny files, so I don't care about it.
