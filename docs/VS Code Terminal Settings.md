# VS Code Terminal Settings
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

The `terminal.integrated.*` settings let you set terminal oprions that will be used by all integrated terminal profiles.

- For example:
    > ```json
    > "terminal.integrated.fontFamily": "Hack",
    > "terminal.integrated.fontSize": 12,
    > "terminal.integrated.fontWeight": "normal",
    > "terminal.integrated.cursorStyle": "line",
    > ```

`"terminal.external.windowsExec": "C:\\WINDOWS\\System32\\cmd.exe",` Sets the *External* terminal to the command prompt.

## Shell Integration
> Shell integration is an experimental feature, which will turn on certain features like enhanced command tracking and current working directory detection. Shell integration works by injecting a script that is run when the shell is initialized and lets the terminal gain additional insights into what is happening within the terminal. Note that the script injection may not work if you have custom arguments defined in the terminal profile.

> Supported shells:
> - Linux/macOS: bash, pwsh, zsh
> - Windows: *pwsh*

> You can try it out by setting: `"terminal.integrated.enableShellIntegration": true,`

## Terminal Settings
```json
"terminal.integrated.profiles.windows": {
    "PowerShell": {
    "source": "PowerShell",
    "icon": "terminal-powershell",
    },
    "Conda": {
    "path": "C:\\WINDOWS\\System32\\cmd.exe",
    "args": ["/K", "C:\\ProgramData\\Anaconda3\\Scripts\\activate.bat C:\\ProgramData\\Anaconda3"],
    "icon": "terminal-bash",
    "color": "terminal.ansiCyan",
    },
    "CondaPS": {
    "source": "PowerShell",
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

```
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

## Default Profile Terminal Settings
- The default profile can be defined manually with the `terminal.integrated.defaultProfile.windows` settings.
- This should be set to the name of an existing profile:
> `"terminal.integrated.defaultProfile.windows": "CondaPS",`
