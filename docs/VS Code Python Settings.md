# VS Code Python Settings

## Workbench Settings
```json
//    "workbench.startupEditor": "newUntitledFile",
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook",
        "*.md": "vscode.markdown.preview.editor"
    },
```


## Python Editor Appearance settings
```json
    "editor.rulers": [80, 120],
    "editor.tabSize": 4,
    "editor.renderWhitespace": "trailing",
```

## File Formatting
```json
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,

    "files.associations": {
        "*.pyx": "python",
        "*.py": "python"
    },
    // "files.autoSave": "onFocusChange",
    // "editor.formatOnSave": true,
    // "editor.defaultFormatter": "esbenp.prettier-vscode",
```

## Editor Suggestion settings
```json
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",

    "editor.suggestSelection": "first",
    "editor.acceptSuggestionOnEnter": "off",
    "editor.suggest.localityBonus": true,
    "editor.inlineSuggest.enabled": true,
```
# DONE TO HERE

## Python run settings
- `"terminal.executeInFileDir"`
    > Indicates whether to run a file in the file's directory instead of the current folder.
    > Default: false
- `"terminal.activateEnvInCurrentTerminal"`
    > Specifies whether to activate the currently open terminal when the Python extension is activated, using the virtual environment selected.
    > Default: false
```json
    // "python.terminal.executeInFileDir": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    // "python.terminal.launchArgs": [ ],
```

## Python formatting settings
```json
    // "python.experiments.enabled": false,
    "[python]": {
        "editor.formatOnSave": false,
        "editor.defaultFormatter": "ms-python.python"
        "Workspace_Formatter.includePattern": ["*.py"]
    },

    "pythonIndent.useTabOnHangingIndent": true,
    "python.analysis.completeFunctionParens": true,
    "python.autoComplete.addBrackets": true,
    "python.formatting.provider": "autopep8",
```

## Python Linting Settings
- `"python.analysis.typeCheckingMode"`
    > Specifies the level of type checking analysis to perform. Available values are:
    - off
        > No type checking analysis is conducted; unresolved imports/variables diagnostics are produced.
    - basic
        > Non-type checking-related rules (all rules in off), as well as basic type checking rules are used.
    - strict
        > All type checking rules at the highest severity of error (including all rules in off and basic categories) are used.

```json
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",

    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,

    "python.linting.pylintEnabled": true,
    "python.linting.pylintUseMinimalCheckers": false,

    "python.linting.mypyEnabled": false,
    "python.linting.flake8Enabled": false,
```


## DocString Settings
```json
    "autoDocstring.includeExtendedSummary": true,
    "autoDocstring.generateDocstringOnEnter": true,
    "autoDocstring.quoteStyle": "'''",

    "docstringFormatter.wrapDescriptionsLength": 79,
```

## Unit Test Settings
```json
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
```

## Jupyter Notebook Settings
```json
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
```

## Spelling words
```json
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
```



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
