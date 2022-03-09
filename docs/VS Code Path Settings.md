# VS Code Path Settings
- One of the big challenges with getting these settings correct is that if there are errors, typos or incorrect path delimiters the setting will fail silently. 

# Python Interpreter Path
## `python.pythonPath` Settings
- For *Global* Anaconda environments the path is 
    > `"C:/ProgramData/Anaconda3/<Environment Name>/python.exe"`
- For *local* (single user) environments the path is 
    > `"C:/Users/${env:USERNAME}.conda/envs/<Environment Name>/python.exe"`
## Default Interpreter Path
> Path to default Python to use when extension loads up for the first time, 
no longer used once an interpreter is selected for the workspace. 
See https://aka.ms/AAfekmf to understand when this is used.
> - `"python.defaultInterpreterPath": "C:/ProgramData/Anaconda3/<Environment Name>/python.exe",`<br>
> **OR**<br>
> - `"python.defaultInterpreterPath": "C:/Users/${env:USERNAME}.conda/envs/<Environment Name>/python.exe",`

# VS Code `.env` Settings
- PYTHONPATH in the .env file must be absolute paths.
- On Windows the slashes in the path lean forward: "/". 
- Different paths are separated with a ";" on Windows.
- It appears tha Variable substitution is only supported for environment variables that are defined earlier in the file.

**Example `.env` file**
> ```
> HOME_PATH="C:\Users\smoke"
> WORKSPACE_FOLDER="${HOME_PATH}/Documents/Python Scripts/TestPathPackage"
> PYTHONPATH="${WORKSPACE_FOLDER};${PYTHONPATH}"
> PYTHONPATH="${WORKSPACE_FOLDER}/tests;${PYTHONPATH}"
> PYTHONPATH="${WORKSPACE_FOLDER}/examples;${PYTHONPATH}"
> PYTHONPATH="${WORKSPACE_FOLDER}/src;${PYTHONPATH}"
> ```

### Path to `.env` file
- `python.envFile` is the path to the "`.env`" file, described above.
- Typical path is:
    - `"python.envFile": "${workspaceFolder}/.env"`

# Settings for pylint 
<b><i>`pylint` depends on the presence of the `__init__.py` and on correct `.env` settings.</i></b>
- Pylint will only search for other modules in the worspace directory if the module from which it is launched is in a folder which is a package (i.e. has _init_.py file)
- The _init_.py file may be empty.  It just needs to exist.

# VS Code *launch.json* Settings
**Debugging**
- Set the working directory to that of the file being executed.
    > The default will be to start in the *workspaceFolder*

- Add import path to the *PYTHONPATH* environment variable.
    > `"env": {"PYTHONPATH": "${workspaceFolder};${env:PYTHONPATH}"}`

- The added import path can either be a full path or a sub-folder of the current working directory.
    > `"env": {"PYTHONPATH": "examples"}`

- This is not nessesary if the *PYTHONPATH* setting in the `.env` file already
 includes the required folders.

- **Example: `launch.json` Settings**
> ```json
> {
>     "version": "0.2.0",
>     "configurations": [
>         {
>             "name": "Python: Current File",
>             "type": "python",
>             "request": "launch",
>             "program": "${file}",
>             "console": "integratedTerminal",
>             "cwd": "${fileDirname}",
>             "justMyCode": true,
>             "env": {"PYTHONPATH": "${workspaceFolder}/tests;${workspaceFolder}/examples;${env:PYTHONPATH}"},
>         }
>     ]
> }
> ```

# Language Server Settings
- **Note:** The language server settings apply when `python.languageServer` is "Pylance" or "Default". 
- The paths are relative to the workspace root directory.
- Paths should be specified as strings and must be separated by commas when there are multiple paths.

### `python.analysis.extraPaths` Language Server settings
> Specifies extra search paths for import resolution. 
> 

### `python.autoComplete.extraPaths` AutoComplete settings
> Specifies locations of additional packages for which to load autocomplete data.

For example:
```json
"python.analysis.extraPaths": [
    "src",
    "examples",
    "tests"
    ],
"python.autoComplete.extraPaths": [
    "src",
    "examples",
    "tests"
    ]
```

# Terminal Settings
### Terminal Profile Settings
> - **path:** The path pointing to the shell executable.
> - **source:** Optional alternative to `path`. Can be either *"PowerShell"*, or *"Git Bash"*.
> - **overrideName:** Replace the dynamic terminal title that detects what program is running with the static profile name.
> - **env:** Defines environment variables and their values.
> - **icon:** An icon ID to use for the profile.
> - **color:** A theme color ID to style the icon.


The `terminal.integrated.env.<platform>` setting lets you explicitly set environment variables that will be added to the VS Code process to be used by all terminal profiles. 

- Set the variable to null to delete it from the environment. This can be configured for all  using the  setting.

- For example:
    > ```json
    > "terminal.integrated.env.windows": {
    >     "PYTHONPATH": "${workspaceFolder}/src;${workspaceFolder}/tests;${workspaceFolder}/examples;${env:PYTHONPATH}"
    > ```



## Default Profile Terminal Settings
- The default profile can be defined manually with the `terminal.integrated.defaultProfile.windows` settings. 
- This should be set to the name of an existing profile:

> ```json
> "terminal.integrated.automationProfile.windows": {
>       "path": "C:\\WINDOWS\\System32\\cmd.exe",
>       "args": [
>         "/K",
>         "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"
>       ],
>        "icon": "terminal-bash",
>        "color": "terminal.ansiCyan",
>     },
> 
> "terminal.integrated.automationProfile.windows": "Conda",
> ```

## Creating a Python command prompt terminal
> ```json
>    "PythonShell": {
>        "path": "C:\\WINDOWS\\System32\\cmd.exe",
>        "args": ["/K", "python.exe"],
>        "overrideName": true,
>        "icon": "terminal-powershell",
>        "color": "terminal.ansiGreen",
>        },
> ```

# pythonPathSetter
### Import path settings
**pythonPathSetter** is an extension that adds import paths
```json
    "pythonPathSetter.sourceDirs": [
      "src",
      "\\\\dkphysicspv1\\e$\\Gregs_Work\\Python Projects\\Utilities"
    ]
```

