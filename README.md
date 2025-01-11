# AutoCleanUpTool
This scripts automatically deletes files based on the configuration.
Simple...

# Declaimar
This script is useful but also dangerous, I'm not responsible for your deleted backups, logs, p*rns and etc.

Make sure you configured it right and test it with dummy files. specially your REGEX value.

I recommend using my example folder and default configuration to see how it works.

# SetUp
## Download the project
### Linux
Clone this repo using git:

```git clone https://github.com/Ashaxer/AutoCleanUpTool.git```

### Windows
Just download the repo and unzip it.

## Requirements
Navigate to the folder and install requirements:
### Linux
```python3 -m pip install -r requirements.txt```

### Windows
```python -m pip install -r requirements.txt```

## Configuration
Edit the "config.env" Configuration file using any text-editor:
### Linux
```nano config.env```

### Windows
:|

# Configuration Options
```PATH```: Path to the location where target files are located.

```ABSOLUTE_PATH``` [True/False]: Indicate PATH type, absolute or not. (Absolute E.X.: D:\Files\Example, Releative E.X. if the target folder is next to the program: Example)

```FILES_TO_KEEP``` [Integer]: Indicate how many files you want to keep, other files will be deleted.

```FILES_PATTERN``` [REGEX]: A regular expression used to filter files inside the target folder.

```DELETE_BY_DATE_MODIFIED``` [True/False]: Indicate how to detect and delete older files, "False" sortes by name.

```LOG_FILE```: Log file path and name

```LOG_ABSOLUTE_PATH``` [True/False]: Indicate LOG_FILE path type, absolute or not. (Absolute E.X.: D:\Files\cleanup_log, Releative E.X.: cleanup_log)



