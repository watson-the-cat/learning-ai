# Terminal Cheat Sheet

Commands you'll use daily. Practice these in the Cursor terminal (Ctrl+`).

## Navigating

| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Print where you are | `pwd` |
| `ls` | List files in current folder | `ls` |
| `ls -la` | List all files with details | `ls -la` |
| `cd folder` | Go into a folder | `cd projects` |
| `cd ..` | Go up one folder | `cd ..` |
| `cd ~` | Go to home directory | `cd ~` |

## Creating and Managing Files

| Command | What it does | Example |
|---------|-------------|---------|
| `mkdir name` | Create a folder | `mkdir my-project` |
| `touch file` | Create an empty file | `touch notes.md` |
| `cp file dest` | Copy a file | `cp data.csv backup.csv` |
| `mv file dest` | Move or rename a file | `mv old.txt new.txt` |
| `rm file` | Delete a file (careful!) | `rm temp.txt` |
| `rm -r folder` | Delete a folder and contents | `rm -r old-project` |

## Reading Files

| Command | What it does | Example |
|---------|-------------|---------|
| `cat file` | Show entire file | `cat README.md` |
| `head file` | Show first 10 lines | `head data.csv` |
| `tail file` | Show last 10 lines | `tail log.txt` |

## Useful Tricks

| Trick | What it does |
|-------|-------------|
| `Tab` key | Auto-complete file/folder names |
| Up arrow | Recall previous commands |
| `Ctrl+C` | Cancel a running command |
| `clear` | Clear the terminal screen |
| `history` | Show command history |

## PowerShell Equivalents

Since you're on Windows, some commands differ in PowerShell:

| Bash (Git Bash) | PowerShell | What it does |
|-----------------|-----------|-------------|
| `ls` | `Get-ChildItem` or `dir` | List files |
| `pwd` | `Get-Location` | Current directory |
| `cat file` | `Get-Content file` | Show file contents |
| `touch file` | `New-Item file` | Create file |
| `rm file` | `Remove-Item file` | Delete file |

**Tip:** Git Bash (installed with Git) uses the Bash commands, which are more universal. You can switch Cursor's default terminal to Git Bash in settings.

## Practice Exercise

Try this sequence in your terminal:

```bash
cd "c:\Users\kevkong\My Drive\Learning AI"
pwd
ls
cd projects
ls
cd 01-first-script
pwd
cd ../..
```
