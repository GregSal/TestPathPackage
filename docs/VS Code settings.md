# VS Code Path settings
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


# DONE TO HERE





```
    "terminal.external.windowsExec": "C:\\WINDOWS\\System32\\cmd.exe",
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.profiles.windows": {
      "PowerShell": {
        "source": "PowerShell",
        "icon": "terminal-powershell",
      },
      "Conda": {
        "path": "C:\\WINDOWS\\System32\\cmd.exe",
        "cursorStyle": "line",
        "args": ["/K", "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"],
        "icon": "terminal-bash",
        "color": "terminal.ansiCyan",
      },
      "CondaPS": {
        "source": "PowerShell",
        "cursorStyle": "line",
        "args": ["-ExecutionPolicy", "ByPass", "-NoExit", "-Command", "& 'C:\\ProgramData\\Anaconda3\\shell\\condabin\\conda-hook.ps1' ; conda activate 'C:\\ProgramData\\Anaconda3'"],
        "icon": "terminal-bash",
        "color": "terminal.ansiCyan",
      },
      "Command Prompt": {
        "path": [
          "${env:windir}\\Sysnative\\cmd.exe",
          "${env:windir}\\System32\\cmd.exe"
        ],
        "args": [],
        "icon": "terminal-cmd"
      },
      "Git Bash": {
        "source": "Git Bash"
      },
    },
    "terminal.integrated.defaultProfile.windows": "CondaPS",
    "terminal.integrated.automationProfile.windows": {
      "path": "C:\\WINDOWS\\System32\\cmd.exe",
      "cursorStyle": "line",
      "args": [
        "/K",
        "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"
      ],
      "icon": "terminal-bash",
      "color": "terminal.ansiCyan",
    },


```
{
"terminal.integrated.profiles.windows": {    
"my-pwsh": {
      "source": "PowerShell",
      "args": ["-NoProfile"]
    }
  },  
"terminal.integrated.defaultProfile.windows": "my-pwsh"
}
```
`%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& %windir%\System32\cmd.exe /K "CALL C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3&&CALL conda activate TestPathDev"`


## Run in terminal
### 


Other arguments supported in profiles include:

> - **overrideName:** A boolean indicating whether or not to replace the dynamic terminal title that detects what program is running with the static profile name.
> - **env:** A map defining environment variables and their values, set the variable to null to delete it from the environment. This can be configured for all profiles using the terminal.integrated.env.<platform> setting.
> - **icon:** An icon ID to use for the profile.
> - **color:** A theme color ID to style the icon.




# VS Code User Settings
## Terminal Settings
    "terminal.external.windowsExec": "C:\\WINDOWS\\System32\\cmd.exe",
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.profiles.windows": {
      "PowerShell": {
        "source": "PowerShell",
        "icon": "terminal-powershell",
      },
      "Conda": {
        "path": "C:\\WINDOWS\\System32\\cmd.exe",
        "cursorStyle": "line",
        "args": ["/K", "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"],
        "icon": "terminal-bash",
        "color": "terminal.ansiCyan",
      },
      "CondaPS": {
        "source": "PowerShell",
        "cursorStyle": "line",
        "args": ["-ExecutionPolicy", "ByPass", "-NoExit", "-Command", "& 'C:\\ProgramData\\Anaconda3\\shell\\condabin\\conda-hook.ps1' ; conda activate 'C:\\ProgramData\\Anaconda3'"],
        "icon": "terminal-bash",
        "color": "terminal.ansiCyan",
      },
      "Command Prompt": {
        "path": [
          "${env:windir}\\Sysnative\\cmd.exe",
          "${env:windir}\\System32\\cmd.exe"
        ],
        "args": [],
        "icon": "terminal-cmd"
      },
      "Git Bash": {
        "source": "Git Bash"
      },
    },
    "terminal.integrated.defaultProfile.windows": "CondaPS",
    "terminal.integrated.automationProfile.windows": {
      "path": "C:\\WINDOWS\\System32\\cmd.exe",
      "cursorStyle": "line",
      "args": [
        "/K",
        "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"
      ],
      "icon": "terminal-bash",
      "color": "terminal.ansiCyan",
    },

# pythonPathSetter
### Import path settings
**pythonPathSetter** is an extension that adds import paths
```json
    "pythonPathSetter.sourceDirs": [
      "src",
      "\\\\dkphysicspv1\\e$\\Gregs_Work\\Python Projects\\Utilities"
    ]
```


# Project Settings *.vscode\settings.json* 
### Python run settings
    "python.terminal.executeInFileDir": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.terminal.launchArgs": [
        ],

## Workbench Settings
    "workbench.startupEditor": "newUntitledFile",
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook",
        "*.md": "vscode.markdown.preview.editor"
    },
    "workbench.editor.untitled.hint": "hidden",
    "workbench.editor.highlightModifiedTabs": true,    

#### Clean up 
```json
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,
    "editor.formatOnSave": true,
//    "editor.defaultFormatter": "esbenp.prettier-vscode",
```
    "files.autoSave": "onFocusChange",
    "files.associations": {
        "*.pyx": "python",
        "*.py": "python"
    },

### Line Markers at **80** and **100** columns
    "editor.rulers": [80, 120],
    "editor.tabSize": 4,
    "editor.renderWhitespace": "trailing",
    "editor.renderLineHighlight": "gutter",
    "editor.cursorSurroundingLines": 2,
    "editor.minimap.enabled": false,

### Editor Suggestion settings
    "editor.suggestSelection": "first",
    "editor.acceptSuggestionOnEnter": "off",
    "editor.suggest.localityBonus": true,
    "editor.inlineSuggest.enabled": true,

    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",

## Python Settings
    "python.experiments.enabled": false,
    "[python]": {
        "editor.formatOnSave": false,
        "editor.defaultFormatter": "ms-python.python"
    },

### Python Linting Settings
    "python.linting.mypyEnabled": false,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintUseMinimalCheckers": false,
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": false,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "autopep8",

    "python.languageServer": "Default",
    "python.languageServer": "Pylance",

### DocString Settings
    "autoDocstring.includeExtendedSummary": true,
    "autoDocstring.quoteStyle": "'''",
    "autoDocstring.generateDocstringOnEnter": true,
    "autoDocstring.quoteStyle": "'''",

    "docstringFormatter.wrapDescriptionsLength": 79,

    "pythonIndent.useTabOnHangingIndent": true,
    "python.analysis.completeFunctionParens": true,
    "python.autoComplete.addBrackets": true,


## Unit Test Settings
    "testExplorer.addToEditorContextMenu": true,
    "testExplorer.mergeSuites": true,

    "pythonTestExplorer.testFramework": "unittest",

    "python.testing.cwd": "./Tests",
    "python.testing.promptToConfigure": true,
    "python.testing.pytestEnabled": false,
    "python.testing.unittestEnabled": true,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": false,
    "python.testing.unittestArgs": [
        "discover",
        "-v",
        "-s",
        "Testing",
        "-p",
        "*tests_*.py"
    ],


## Jupyter Notebook Settings
    "jupyter.pythonExportMethod": "nbconvert",
    "jupyter.stopOnFirstLineWhileDebugging": false,
    "jupyter.themeMatplotlibPlots": true,
    "jupyter.sendSelectionToInteractiveWindow": true,
    "jupyter.askForKernelRestart": false,
    "jupyter.interactiveWindowMode": "perFile",
    "jupyter.jupyterServerType": "local",
    "jupyter.changeDirOnImportExport": true,


    "notebook.compactView": false,
    "notebook.consolidatedRunButton": true,
    "notebook.outline.showCodeCells": true,
    "notebook.diff.ignoreMetadata": true,
    "notebook.diff.ignoreOutputs": true,
    "notebook.lineNumbers": "on",
    "notebook.cellToolbarLocation": {
      "default": "right",
      "jupyter-notebook": "left"
    },
    "notebook.cellFocusIndicator": "border",
    "notebook.showFoldingControls": "always",

## Git settings
    "git.enableSmartCommit": true,
    "git.autofetch": true,
    "git.autorefresh": false,
    "git.confirmSync": false,

#### Trust folder setting
`    "security.workspace.trust.untrustedFiles": "open",`

## Explorer Settings
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "explorer.copyRelativePathSeparator": "/",


## TODO Highlight Settings
#### better-comments
  "better-comments.tags": [
    {
      "tag": "!",
      "color": "#98C379",
      "strikethrough": false,
      "backgroundColor": "transparent"
    },
    {
      "tag": "?",
      "color": "#FF8C00",
      "strikethrough": false,
      "backgroundColor": "transparent"
    },
    {
      "tag": "//",
      "color": "#3498DB",
      "strikethrough": true,
      "backgroundColor": "transparent"
    },
    {
      "tag": "xx",
      "color": "#FF2D00",
      "strikethrough": true,
      "backgroundColor": "transparent"
    },
    {
      "tag": "*",
      "color": "#FF8C00",
      "strikethrough": false,
      "backgroundColor": "transparent"
    }
  ],
  "better-comments.highlightPlainText": true,

#### todo-tree
    "todo-tree.highlights.enabled": false,
    "todo-tree.highlights.customHighlight": {
      "Question": {
        "icon": "question",
        "iconColour": "red",
        "background ": "black",
        "type": "text"
      },
      "TODO": {
        "icon": "check",
        "type": "text"
      },
      "FIXME": {
        "icon": "alert",
        "foreground": "black",
        "iconColour": "yellow",
        "type": "line"
      },
      "Done To Here": {
        "icon": "arrow-right",
        "iconColour": "#50FF00",
        "type": "tag"
      }
  },
  "todo-tree.highlights.defaultHighlight": {
    "icon": "alert",
    "type": "text",
    "foreground": "red",
    "background": "white",
    "opacity": 50,
    "iconColour": "blue"
    },
    "todo-tree.regex.regexCaseSensitive": false,
    "todo-tree.tree.showCountsInTree": true,
    "todo-tree.general.statusBar": "tags",
    "todo-tree.general.tags": [
      "TODO",
      "FIXME",
      "Question",
      "Done To Here"
    ],
#### todohighlight
    "todohighlight.isCaseSensitive": true,
    "todohighlight.isEnable": true,
    "todohighlight.keywords": [
      "DEBUG:",
      "REVIEW:",
      {
        "text": "NOTE",
        "color": "#ff0000",
        "backgroundColor": "yellow",
        "overviewRulerColor": "grey"
      },
      {
        "text": "Question",
        "color": "#000",
        "backgroundColor": "cyan",
        "isWholeLine": false
      },
      {
        "text": "FIXME",
        "color": "red",
        "border": "1px solid red",
        "borderRadius": "2px",
        //NOTE: using borderRadius along with `border` or you will see nothing change
        "backgroundColor": "rgba(0,0,0,.2)"
        //other styling properties goes here ...
      },
      {
        "text": "TODO",
        "color": "#ff0000",
        "backgroundColor": "#87CEFA",
        "overviewRulerColor": "yellow"
      },
      {
        "text": "Done To Here",
        "color": "#000",
        "backgroundColor": "#00FF00",
        "overviewRulerColor": "yellow",
        "fontWeight": "bold"
      },
    ],
    "todohighlight.include": [
      "**/*.js",
      "**/*.jsx",
      "**/*.py",
      "**/*.xml",
      "**/*.html",
      "**/*.css",
      "**/*.scss"
    ],
    "todohighlight.exclude": [
      "**/node_modules/**",
      "**/bower_components/**",
      "**/dist/**",
      "**/build/**",
      "**/.vscode/**",
      "**/.github/**",
      "**/_output/**",
      "**/*.min.*",
      "**/*.map",
      "**/.next/**"
    ],

## Spelling words
    "cSpell.userWords": [
      "arange",
      "disp",
      "dropna",
      "DVHs",
      "etree",
      "fstring",
      "gsal",
      "iloc",
      "indx",
      "inplace",
      "interp",
      "isgeneratorfunction",
      "mkdir",
      "ndarray",
      "numpy",
      "pylint",
      "pyplot",
      "rmdir",
      "rsplit",
      "Salomons",
      "scipy",
      "Sectionary",
      "struct",
      "varkw"
      "xlwings"
    ],
    "cSpell.language": "en,en-GB",
    "cSpell.enableFiletypes": [
      "!c",
      "!cpp",
      "!go",
      "!handlebars",
      "!haskell",
      "!jade",
      "!php",
      "!pug",
      "bat",
      "jupyter",
      "sql",
      "xml"
    ],



### Theme Settings
    "workbench.iconTheme": "vscode-great-icons",
    "workbench.colorTheme": "Default High Contrast",
    "workbench.colorTheme": "Solarized Light",
    "workbench.colorTheme": "Visual Studio Light",
    "workbench.colorTheme": "Monokai",
    "workbench.colorTheme": "Quiet Light",

    "materialTheme.accent": "Cyan",
  

## MSSQL Settings
    "mssql.connections": [
      {
        "server": "{{put-server-name-here}}",
        "database": "{{put-database-name-here}}",
        "user": "{{put-username-here}}",
        "password": ""
      }
    ],

## Random Stuff
    "kite.showWelcomeNotificationOnStartup": false,
    "[jsonc]": {
      "editor.defaultFormatter": "esbenp.prettier-vscode"
    },
    "[xml]": {
      "editor.defaultFormatter": "DotJoshJohnson.xml"
    },
    // IntelliSense AI Extension
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    // Formatter extensions
    "Workspace_Formatter.includePattern": ["*.py"]
  "search.useGlobalIgnoreFiles": true,
  "vsicons.dontShowNewVersionMessage": true,
  "xmlTools.enableXmlTreeViewCursorSync": true,
  "bookmarks.saveBookmarksInProject": true,


## Guides settings
    "guides.limit.maximum": 0.3,
    "guides.active.width": 2,
    "guides.normal.width": 2,
    "guides.overrideDefault": true,
    "guides.stack.width": 2,
    "guides.active.style": "groove",
    "guides.active.gutter": true,
    "guides.active.expandBrackets": true,






## Project Manager Settings
    "projectManager.git.baseFolders": [
      "A:\\OneDrive - Queen's University\\Python\\Projects"
    ],




# python.analysis.typeCheckingMode	Setting
- off	
- Specifies the level of type checking analysis to perform. Available values are off, basic, and strict. When set to off no type checking analysis is conducted; unresolved imports/variables diagnostics are produced. When set to basic non-type checking-related rules (all rules in off), as well as basic type checking rules are used. When set to strict all type checking rules at the highest severity of error (including all rules in off and basic categories) are used.


#### Notes
- One of the big challenges with getting these settings correct is that if there are errors, typos 
or incorrect path delimiters the setting will fail silently. 
- On Windows the slashes in the path lean forward: "/". 
- Different paths are separated with a ";" on Windows and a ":" on other platforms with.
- `${pathSeparator}` is not ":" or ";". `${pathSeparator}` is "/" for Linux/Mac or "\" for Windows
- `${workspaceFolder}` evaluates to *myproject*, it is not to the *.vscode* folder.
- `${workspaceFolder}` will be relative to the scripts folder.
- `"terminal.integrated.cwd": "${workspaceFolder}"`, ***doesn't work???***
- It is not clear if the vscode *.env* file does variable expansion such as: `${WORKSPACE_FOLDER}`.
>> "Variable substitution is only supported in VS Code settings files, it will not work in *.env* 
environment files." [VS Code Environment variables](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file "VS Code Environment variables")

>> On that same page it says: "values can refer to any other environment variable that's already 
defined in the system or earlier in the file", which is what we're doing here. It seems the 
documentation is contradicting itself. 
>> *Tip:* Path, args, and env all support resolving variables.

- Make sure that you have configured VS Code to allow terminal configurations to amend your shell 
settings (via Manage Workspace Shell Permissions ***????***) 
[VS Code Integrated Terminal Settings](https://code.visualstudio.com/docs/editor/integrated-terminal#_configuration). 
Otherwise VS Code silently ignores your `terminal.integrated.env.{platform}` settings.
> Does the above comment refer to this?
>>Shell integration is an experimental feature, which will turn on certain features like enhanced 
command tracking and current working directory detection. Shell integration works by injecting a 
script that is run when the shell is initialized and lets the terminal gain additional insights 
into what is happening within the terminal. Note that the script injection may not work if you 
have custom arguments defined in the terminal profile.
>> Supported shells:
>> - Linux/macOS: bash, pwsh, zsh
>> - Windows: *pwsh*
>> You can try it out by setting: `terminal.integrated.enableShellIntegration` to true.
