# startkit

A skeleton generator for python projects.

## Installation

```cmd
pip install startkit
```

## Usage Demo

```cmd
cd C:\workspace
startkit

> Where will the project be created? [C:\workspace]
> Please enter your project name: [myproject]
> Please enter main package name: [myproject]
> Please enter your project version: [0.0.1]
> Please enter your project description: *********
> Please enter your name: [***] ******
> Please enter your email: ******@***.com

The project has been created successfully!

To get started:

  cd C:\workspace\myproject
  venv\Scripts\activate.bat (cmd.exe)
  venv\Scripts\Activate.ps1 (PowerShell)
  source venv/bin/activate (bash/zsh)
  pip install -r requirements.txt
  pip freeze > requirements.txt
  python -m myproject
  ...
  deactivate

Documentation can be found at https://pypi.org/project/startkit.
```

**warning**: The text in "()" is just explanatory text. Don't paste them to run.

**warning**: For more executable commands, refer to the "Makefile" of the project.

## Bug Reports

If you have any bugs to report, you're welcome to file an [issue](https://github.com/niemingzhao/startkit/issues).
