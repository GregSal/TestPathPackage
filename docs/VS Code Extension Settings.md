# VS Code Python Settings

## Random Stuff
```json
    "kite.showWelcomeNotificationOnStartup": false,
    "vsicons.dontShowNewVersionMessage": true,
    "search.useGlobalIgnoreFiles": true,
    // "xmlTools.enableXmlTreeViewCursorSync": true,
    // "bookmarks.saveBookmarksInProject": true,
    // "[jsonc]": {
    // "editor.defaultFormatter": "esbenp.prettier-vscode"
    // },
    // "[xml]": {
    // "editor.defaultFormatter": "DotJoshJohnson.xml"
    // },

    // Formatter extensions
```

## Workbench Settings
```json
//    "workbench.startupEditor": "newUntitledFile",
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook",
        "*.md": "vscode.markdown.preview.editor"
    },
    "workbench.editor.untitled.hint": "hidden",
    "workbench.editor.highlightModifiedTabs": true,
```

## Clean up
```json
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,
//    "editor.formatOnSave": true,
//    "editor.defaultFormatter": "esbenp.prettier-vscode",
```

## Python Editor Appearance settings
```json
    "editor.rulers": [80, 120],
    "editor.tabSize": 4,
    "editor.renderWhitespace": "trailing",
    "editor.renderLineHighlight": "gutter",
    "editor.cursorSurroundingLines": 2,
    "editor.minimap.enabled": false,
```
## Editor Suggestion settings
```json
    "editor.suggestSelection": "first",
    "editor.acceptSuggestionOnEnter": "off",
    "editor.suggest.localityBonus": true,
    "editor.inlineSuggest.enabled": true,

    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
```
# DONE TO HERE

## Python run settings
```json
    "python.terminal.executeInFileDir": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.terminal.launchArgs": [
        ],
```

```json
    "files.autoSave": "onFocusChange",
    "files.associations": {
        "*.pyx": "python",
        "*.py": "python"
    },
```

## Python Settings
    "python.experiments.enabled": false,
    "[python]": {
        "editor.formatOnSave": false,
        "editor.defaultFormatter": "ms-python.python"
    "Workspace_Formatter.includePattern": ["*.py"]
    },

## Python Linting Settings
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

## DocString Settings
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



{
    "code-runner.executorMap": {
        "python": "python -u",
        "powershell": "powershell -ExecutionPolicy ByPass -File",
        "bat": "cmd /c",
        "csharp": "scriptcs",
        "vbscript": "cscript //Nologo"
    },


    "tabnine.experimentalAutoImports": true,


    "pythonPathSetter.sourceDirs": [
      "src",
      ".",
      "C:\\\\Users\\\\gsalomon\\\\OneDrive - Queen's University\\\\Python\\\\Projects\\\\Utilities"
    ],


    "mssql.connections": [
      {
        "server": "{{put-server-name-here}}",
        "database": "{{put-database-name-here}}",
        "user": "{{put-username-here}}",
        "password": ""
      }
    ],


    "path-intellisense.absolutePathToWorkspace": false,


    "xmlTools.enableXmlTreeViewCursorSync": true


    "sync.autoDownload": true,
    "sync.autoUpload": true,


  "spellright.addToSystemDictionary": true,
  "spellright.language": [
      "en"
  ],
  "spellright.documentTypes": [
      "markdown",
      "latex",
      "plaintext",
      "python"
  ],
  "spellright.notificationClass": "hint",


    "gitlens.menus": {
        "editor": {
            "blame": false,
            "clipboard": true,
            "compare": true,
            "details": false,
            "history": true,
            "remote": false
        },
        "editorGroup": {
            "blame": true,
            "compare": true
        },
        "editorTab": {
            "clipboard": true,
            "compare": true,
            "history": true,
            "remote": true
        },
        "explorer": {
            "clipboard": true,
            "compare": true,
            "history": true,
            "remote": true
        },
        "scmGroup": {
            "compare": true,
            "openClose": true,
            "stash": true,
            "stashInline": true
        },
        "scmItem": {
            "clipboard": true,
            "compare": true,
            "history": true,
            "remote": true,
            "stash": true
        }
    },
    "gitlens.views.repositories.location": "scm",
    "gitlens.views.fileHistory.location": "explorer",
    "gitlens.views.lineHistory.location": "explorer",
    "gitlens.views.compare.location": "gitlens",
    "gitlens.views.search.location": "gitlens",





## Project Manager Settings
    "projectManager.git.baseFolders": [
      "A:\\OneDrive - Queen's University\\Python\\Projects"
    ],

## Sync Settings
```json
{
    "ignoreUploadFiles":[
        "projects.json",
        "projects_cache_vscode.json",
        "projects_cache_git.json",
        "projects_cache_svn.json",
        "gpm_projects.json",
        "gpm-recentItems.json"
        ],
    "ignoreUploadFolders":["workspaceStorage"],
    "ignoreExtensions":[],
    "replaceCodeSettings":{},
    "gistDescription":"Visual Studio Code Settings Sync Gist",
    "version":323,
    "token":"",
    "downloadPublicGist":false,
    "supportedFileExtensions":[
        "json",
        "code-snippets"
        ],
    "openTokenLink":true,
    "disableUpdateMessage":false,
    "lastUpload":null,
    "lastDownload":null,
    "githubEnterpriseUrl":null,
    "askGistName":false,
    "customFiles":{},
    "hostName":null
}
```

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
