# Progress Notes
## `.env` file
1. Added `"python.envFile": "${workspaceRoot}/.env"` to workspace settings:
```
	"settings": {
		"python.envFile": "${workspaceRoot}/.env",
	},
```
with the `.env` file containing:
```
HOME_PATH="${USERPROFILE}"
WORKSPACE_FOLDER="${HOME_PATH}/Documents\\Python Scripts/TestPathPackage"
PYTHONPATH="${WORKSPACE_FOLDER}/tests;${WORKSPACE_FOLDER};${WORKSPACE_FOLDER}/examples;${WORKSPACE_FOLDER}/src;${PYTHONPATH}"
```
- This had no effect when using `Run Python File`
![Run Python File](Run_Python_File.png)

2. Added `launch` configuration 
(required to use `Run and Debug`) ![Run and Debug](RunandDebug.png) 
to workspace settings:
```
"launch": {
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${fileDirname}",
            "env": {"PYTHONPATH": "${workspaceFolder}/src;${env:PYTHONPATH}"},
            "justMyCode": true
        }
    ]
}
```
- This had no effect when using `Run Python File`
![Run Python File](Run_Python_File.png)

- Using `Run and Debug`
![Run and Debug](RunandDebug.png)
Got the following output:
```
In module: __main__
current path is: C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples

PythonPaths:
        c:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Documents\Python Scripts\TestPathPackage\tests
        C:\Documents\Python Scripts\TestPathPackage
        C:\Documents\Python Scripts\TestPathPackage\examples
        C:\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\.conda\envs\TestPathDev\python39.zip
        C:\Users\smoke\.conda\envs\TestPathDev\DLLs
        C:\Users\smoke\.conda\envs\TestPathDev\lib
        C:\Users\smoke\.conda\envs\TestPathDev
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32\lib
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\Pythonwin

In module: simple_script

current path is: C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples

PythonPaths:
        c:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Documents\Python Scripts\TestPathPackage\tests
        C:\Documents\Python Scripts\TestPathPackage
        C:\Documents\Python Scripts\TestPathPackage\examples
        C:\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\.conda\envs\TestPathDev\python39.zip
        C:\Users\smoke\.conda\envs\TestPathDev\DLLs
        C:\Users\smoke\.conda\envs\TestPathDev\lib
        C:\Users\smoke\.conda\envs\TestPathDev
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32\lib
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\Pythonwin

Done module: simple_script


Tomorrow is: Friday, 04. March 2022 09:00AM

Done module: __main__


PS C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples> 
```
***Path Roots:***
PythonPaths:<br>
> <u>*c:\Users\smoke\Documents\Python Scripts*</u>\TestPathPackage\examples<br>
> <u>**C:\Documents\Python Scripts**</u>\TestPathPackage\tests<br>
> <u>**C:\Documents\Python Scripts**</u>\TestPathPackage<br>
> <u>**C:\Documents\Python Scripts**</u>\TestPathPackage\examples<br>
> <u>**C:\Documents\Python Scripts**</u>\TestPathPackage\src<br>
> <u>*C:\Users\smoke\Documents\Python Scripts*</u>\TestPathPackage\src<br>
> <u>*C:\Users\smoke\Documents\Python Scripts*</u>\TestPathPackage\examples<br>
> C:\Users\smoke\.conda\envs\TestPathDev\python39.zip<br>
> ...
- Where is  <u>**C:\Documents**</u> rather than <u>*c:\Users\smoke\Documents*</u> coming from?

3. Removed `"python.envFile": "${workspaceRoot}/.env"` from workspace settings:
- This had no effect

4. Removed the `.env` file
- Using `Run and Debug`
![Run and Debug](RunandDebug.png)
Got the following output:

```
...
PythonPaths:
        c:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\.conda\envs\TestPathDev\python39.zip
        C:\Users\smoke\.conda\envs\TestPathDev\DLLs
        C:\Users\smoke\.conda\envs\TestPathDev\lib
        C:\Users\smoke\.conda\envs\TestPathDev
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32\lib
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\Pythonwin
...
```

- The <u>**C:\Documents**</u> paths disappeared.


5. Modified `.env` file to explicitly state the path:
```
HOME_PATH="C:\Users\smoke"
WORKSPACE_FOLDER="${HOME_PATH}/Documents/Python Scripts/TestPathPackage"
PYTHONPATH="${WORKSPACE_FOLDER}/tests;${WORKSPACE_FOLDER};${WORKSPACE_FOLDER}/examples;${WORKSPACE_FOLDER}/src;${PYTHONPATH}"
```
- The paths are now all correct.
- some duplicates are present.
```
...
PythonPaths:
        c:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\tests
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples
        C:\Users\smoke\Documents\Python Scripts\TestPathPackage\src
        C:\Users\smoke\.conda\envs\TestPathDev\python39.zip
        C:\Users\smoke\.conda\envs\TestPathDev\DLLs
        C:\Users\smoke\.conda\envs\TestPathDev\lib
        C:\Users\smoke\.conda\envs\TestPathDev
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\win32\lib
        C:\Users\smoke\.conda\envs\TestPathDev\lib\site-packages\Pythonwin
...
```

6. Tried setting envireoment variables in the batch file that calls VS Code.
#### VS Code (TestPathDev).bat
```
rem ########## VS Code Launch ############
CALL C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
CALL conda activate TestPathDev
set WORKSPACE_FOLDER="%HOMEPATH%\Documents\Python Scripts\TestPathPackage"
set WORKSPACE_FILE="%WORKSPACE_FOLDER%\TestPathPackage.code-workspace"
Cd "%WORKSPACE_FOLDER%"
C:
code TestPathPackage.code-workspace
```

- Modifiled the `.env` file to match:
```
#HOME_PATH="C:\Users\smoke"
#WORKSPACE_FOLDER="${HOME_PATH}/Documents/Python Scripts/TestPathPackage"
PYTHONPATH="${WORKSPACE_FOLDER}/tests;${WORKSPACE_FOLDER};${WORKSPACE_FOLDER}/examples;${WORKSPACE_FOLDER}/src;${PYTHONPATH}"
```
- *example_script.py* still ran correctly, but pylint gave an import error:
![import_error](import_error.png)

- The %WORKSPACE_FOLDER% environment variable set in the VS Code batch file did not propegate (Not surprising)

*PythonPaths:*<br>
> c:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples<br>
> **C:\tests**<br>
> C:\Users\smoke\Documents\Python Scripts\TestPathPackage\examples<br>
> **C:\examples**<br>
> **C:\src**<br>
> C:\Users\smoke\Documents\Python Scripts\TestPathPackage\src<br>
> ...

<b><i>`pylint` depend on the prsenece of the `__init__.py` and on correct `.env` settings.</i></b>