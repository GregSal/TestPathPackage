rem ########## VS Code Launch ############
set WORKSPACE_FOLDER="%HOMEPATH%\Documents\Python Scripts\TestPathPackage"
set WORKSPACE_FILE="%WORKSPACE_FOLDER%\TestPathPackage.code-workspace"

CALL C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3
CALL conda activate TestPathDev
Cd "%WORKSPACE_FOLDER%"
C:
code TestPathPackage.code-workspace
