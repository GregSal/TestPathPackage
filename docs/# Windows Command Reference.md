# Windows Command Reference

## Check PYTHONPATH Environment variable with:
> - **PowerShell**:  `$Env:PYTHONPATH`
> - **Windows cmd**:  `echo %PYTHONPATH%`

- Print each entry of Windows PYTHONPATH variable on a new line:
> `echo %PYTHONPATH:;=&echo.%`

## Set Environment Variable For The Current Terminal Session

> - **PowerShell**:  `$env:VAR_NAME="VALUE"`
> - **Windows cmd**:  `set VAR_NAME="VALUE"`

## Permanently set an environment variable for the current user
- Run as Administrator. The setx command requires elevated command prompt. 
- The setx command works both for the Windows command-line prompt (CMD) and the Windows PowerShell.
- To see the changes after running setx – open a new command prompt.
> `setx VAR_NAME "VALUE"`

