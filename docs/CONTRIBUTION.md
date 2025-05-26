# Contribution Guide

Welcome! If you're new to GitHub and want to contribute to this project, follow these simple steps. This guide assumes you already have [Git](https://git-scm.com/) installed and a [GitHub account](https://github.com/).

## 1. Fork the Repository

1. Go to the project repository on GitHub.
2. Click the **Fork** button (top right) to create your own copy of the repository.

## 2. Clone Your Fork

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/CSEC_322_FINAL_PROJECT.git
cd CSEC_322_FINAL_PROJECT
```
Replace `YOUR-USERNAME` with your GitHub username.

## 3. Add the Original Repository as a Remote

This lets you keep your fork up to date with the main project.

```bash
git remote add upstream https://github.com/ORIGINAL-OWNER/CSEC_322_FINAL_PROJECT.git
```
Replace `ORIGINAL-OWNER` with the main repository owner's username.

## 4. Create a New Branch

Always create a new branch for your changes:

```bash
git checkout -b your-feature-branch
```
Replace `your-feature-branch` with a descriptive name for your changes.

## 5. Fetch and Rebase (Keep Your Branch Updated)

Before you start working and before you push your changes, make sure your branch is up to date:

```bash
git fetch upstream
git rebase upstream/main
```
If you see any conflicts, Git will tell you what to do. Fix the conflicts, then run:

```bash
git add .
git rebase --continue
```

## 6. Make Your Changes

Edit the files you want to change. Save your work.

## 7. Commit and Push

```bash
git add .
git commit -m "Describe your changes"
git push origin your-feature-branch
```

## 8. Create a Pull Request

1. Go to your fork on GitHub.
2. Click **Compare & pull request**.
3. Add a title and description, then click **Create pull request**.

---

**Need help?** Ask in the project discussions or issues!

Thank you for contributing!
