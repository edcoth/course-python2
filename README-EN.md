# Git Command Summary (Easy to Read)

This document organizes the Git commands you provided into a clear, easy-to-read cheat sheet with short explanations and examples.

---

## User configuration (global)
Before you start using Git, set your username and email so commits show the correct author.

- Set your username:
```bash
git config --global user.name "YourGitHubUsername"
```

- Set your email:
```bash
git config --global user.email "you@example.com"
```

- Check credential helper (how Git remembers credentials):
```bash
git config --global credential.helper
```
Common helpers:
- cache — temporarily stores credentials in memory
- store — saves credentials in plaintext (not secure on shared machines)
- osxkeychain / wincred / manager-core — OS-native credential managers

- View all Git configuration:
```bash
git config --list
```

---

## Initialize repository and manage files
- Initialize a Git repository in the current folder:
```bash
git init
```

- Add all files to the staging area:
```bash
git add .
```
Note: To add specific files, replace `.` with filenames.

- Create a commit with a message:
```bash
git commit -m "Your commit message describing the changes"
```

---

## Branches
- Rename the current branch to `main`:
```bash
git branch -M main
```

- Create and switch to a new branch:
```bash
git switch -c new-branch
# or (older command)
git checkout -b new-branch
```

---

## Remote (GitHub) connection and push
- Add a remote named `origin` (example for GitHub):
```bash
git remote add origin https://github.com/your-username/your-repo.git
```

- Check configured remotes:
```bash
git remote -v
```

- Push local `main` branch to remote and set upstream:
```bash
git push -u origin main
```
The `-u` flag sets the tracking relationship so future `git push` and `git pull` are simpler.

---

## Inspecting status and history
- See current repository status (changed, staged, untracked files):
```bash
git status
```

- View commit history in a compact graphical form:
```bash
git log --oneline --graph --decorate --all
```

---

## Tips and warnings
- Replace `YourGitHubUsername` and `you@example.com` with your real GitHub username and email.
- Avoid `credential.helper store` on shared machines because it writes credentials in plaintext.
- Confirm remote URL is correct and you have permission to push to the repository.
- For SSH-based remotes, use:
```bash
git remote add origin git@github.com:owner/repo.git
```

---

If you want, I can also:
- shorten this into a one-page cheat-sheet,
- produce a printable PDF,
- or commit this file into your repository for you (I'll need repo details and permission).