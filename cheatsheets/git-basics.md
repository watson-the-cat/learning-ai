# Git Cheat Sheet

Git is a save-point system. You make changes, save snapshots (commits), and sync them to GitHub/GitLab.

## The Core Workflow (90% of what you'll do)

```
1. Make changes to files
2. git add .              (stage all changes)
3. git commit -m "message" (save a snapshot)
4. git push               (upload to GitHub/GitLab)
```

## Setup (One Time)

| Command | What it does |
|---------|-------------|
| `git config --global user.name "Your Name"` | Set your name for commits |
| `git config --global user.email "you@email.com"` | Set your email for commits |
| `git init` | Turn a folder into a Git repo |
| `git clone URL` | Download a repo from GitHub/GitLab |

## Daily Commands

| Command | What it does | When to use |
|---------|-------------|-------------|
| `git status` | Show what's changed | Before committing — see what's new |
| `git add .` | Stage all changes | After making changes you want to keep |
| `git add file` | Stage one file | When you only want to commit specific files |
| `git commit -m "msg"` | Save a snapshot | After staging, to record your changes |
| `git push` | Upload to remote | After committing, to share/backup |
| `git pull` | Download latest changes | Before starting work, to get updates |
| `git log --oneline` | Show commit history | To see what's been done |

## Branching (Collaboration Pattern)

Branches let you work on something without affecting the main code:

| Command | What it does |
|---------|-------------|
| `git branch` | List all branches |
| `git branch name` | Create a new branch |
| `git checkout name` | Switch to a branch |
| `git checkout -b name` | Create AND switch (shortcut) |
| `git merge name` | Merge a branch into current |

### Typical branch workflow:

```bash
git checkout -b my-feature    # create a branch for your work
# ... make changes ...
git add .
git commit -m "add feature"
git push -u origin my-feature # push branch to remote
# Then create a Merge Request (GitLab) or Pull Request (GitHub)
```

## Undoing Things

| Command | What it does | Safety |
|---------|-------------|--------|
| `git checkout -- file` | Undo changes to a file | Safe |
| `git reset HEAD file` | Unstage a file | Safe |
| `git stash` | Temporarily hide changes | Safe — use `git stash pop` to get them back |

## GitHub vs GitLab

| Concept | GitHub | GitLab |
|---------|--------|--------|
| Share code changes | Pull Request (PR) | Merge Request (MR) |
| Automated testing | GitHub Actions | GitLab CI/CD |
| NVIDIA uses | For open source | For internal projects |

## .gitignore

A `.gitignore` file tells Git which files to skip (not track). Common entries:

```
__pycache__/
*.pyc
.env
.DS_Store
node_modules/
```

## Practice Exercise

Try this in your terminal:

```bash
cd "c:\Users\kevkong\My Drive\Learning AI"
git status
git log --oneline
git branch
```
