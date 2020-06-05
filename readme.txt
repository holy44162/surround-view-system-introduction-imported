solve problem: PyLint not recognizing cv2 members
1. C:\Users\James\AppData\Roaming\Python\Python38\Scripts\pylint.exe --generate-rcfile > .pylintrc
2. At the beginning of the generated .pylintrc file you will see

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code.
extension-pkg-whitelist=
Add cv2 so you end up with

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code.
extension-pkg-whitelist=cv2
Save the file. The lint errors should disappear.