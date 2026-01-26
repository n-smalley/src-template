# Git Best Practices and Workflow
## 1) Common Terminology
| Term                  | What it means                                         | VS Code Tip / CLI                       |
| --------------------- | ----------------------------------------------------- | --------------------------------------- |
| **Repository (repo)** | A project folder tracked by Git                       | VS Code: Open folder → Source Control   |
| **Local repo**        | Your copy of the repo on your machine                 | N/A                                     |
| **Remote repo**       | The repo on GitHub or another server                  | `origin` = default remote               |
| **Branch**            | A version of the code, allows parallel work           | Bottom-left branch picker               |
| **Local branch**      | Branch on your machine                                | `git branch`                            |
| **Remote branch**     | Branch on GitHub (e.g., `origin/main`)                | `git fetch` / `git pull`                |
| **Commit**            | A snapshot of changes                                 | Source Control → Commit button          |
| **Push**              | Upload local commits to GitHub                        | `git push`                              |
| **Pull**              | Download remote changes to local                      | `git pull`                              |
| **Merge**             | Combine branches into one                             | Done via PR in GitHub                   |
| **Pull Request (PR)** | A request to merge your branch into `main`            | VS Code GitHub extension                |
| **Fork**              | A copy of someone else’s repo you control             | Mainly for open-source contributions    |
| **Clone**             | Download a remote repo to your machine                | `git clone <repo-url>`                  |
| **Conflict**          | When changes clash between branches                   | VS Code shows “<<<<<<< >>>>>>>” markers |
| **Squash & Merge**    | Combine all commits in a PR into one commit on `main` | GitHub PR merge option                  |
| **Merge Commit**      | Keep all commits + create a merge commit              | GitHub PR merge option                  |

---

## 2) Best Practices
- Never commit directly to `main` branch
- Work on **feature branches** named clearly:
    - `feature/login`
    - `fix/navbar`
    - or simply `working`
- Pull frequently to stay in sync
- Commit small, logical changes often
- Write **clear** commit messages
    - Good: `Added validation to form`
    - Bad: `fixed stuff`
- Use **Pull Requests** for merging into `main`
- **Squash & Merge** is preferred

---

## 3) Workflow
### Pull Latest `main`
- VS Code:
    - **Source Control** -> **...** -> **Pull**
- CLI:
    - `git pull origin main`

### Create a branch
- VS Code:
    - Branch Picker -> **Create new branch**
- CLI:
    - `git checkout -b branch_name`

### Make changes and commit
- Edit files within working branch
- VS Code:
    - **Source Control** -> **Stage** -> **Commit** -> **Write message** -> **Commit**
- CLI:
    ```bash
    git add .
    git commit -m "Add validation to login form"
    ```

### Push branch to GitHub
- VS Code:
    - **Publish Branch** -> **Sync Changes**
- CLI:
    - `git push origin branch_name`

### Open a Pull Request
- GitHub:
    - **Compare and Pull Request**
- VS Code:
    - GitHub Pull Request extension -> **Create PR** (Next to PR Dropdown)
- CLI:
    - *No CLI for PR*

### Review and Update PR (Repo owner only)
- GitHub / VS Code:
    - Approve or request changes
    - Make changes on **same branch**, commit, push -> PR updates automatically

### Merge the PR (Repo owner only)
- GitHub / VS Code:
    - **Squash & Merge** is preferred method
    - Delete branch after merge
        - VS Code:
            - **Branch Picker** -> **Right-click branch** -> **Delete Branch**
        - CLI:
            `git branch -d branch_name`

### Clean up local version
- Switch back to (checkout) `main`, pull latest, delete local working branch (if not already)
- VS Code:
    - **Synchronize Changes** (bottom left hand corner next to status name)
    - follow delete instructions above
- CLI:
    ```bash
    git checkout main
    git pull
    git branch -d feature/login-form
    ```
---

## 4) Handling Conflicts
- Pull `main` frequently
- VS Code highlights conflicts during merge
    - **Accept Current** / **Accept Incoming** / **Accept Both**
- Commit the resolution and push

## 5) VS Code / CLI Mapping
| Action               | VS Code                    | CLI               |
| -------------------- | -------------------------- | ----------------- |
| Pull latest          | Pull                       | `git pull`        |
| Create branch        | Branch picker → New Branch | `git checkout -b` |
| Commit               | Source Control → Commit    | `git commit`      |
| Push                 | Sync / Publish             | `git push`        |
| Switch branch        | Branch picker              | `git checkout`    |
| View remote branches | N/A                        | `git branch -r`   |


