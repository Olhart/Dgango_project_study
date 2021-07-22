git config --global user.name "Olhart"
git config --global user.email olhart266@gmail.com
git config --list
git config user.name
git config --global color.ui true
git init
git add .$ 
git commit -m 'initial project version'
git commit --amend
git reset HEAD <file> | git restore --staged <file>
git checkout -- <file> | git restore <file>
git clone https://github.com/libgit2/libgit2 newrepo
git status
git diff (--staged | cached)
git log (-p -2)
git log -p --word-diff | --stat | --shotstat | --name-only | --name-status | --relative-date
git log --pretty (oneline short medium full fuller email raw format<string>) --graph
git log --pretty=format:"%h - %an, %ar : %s"
git log (--all-match) -(n) | --since, --after (=5.mount) | --until,--before | --autor | --committer | --grep | -S | --no-merges
git branch --list
git branch new_branch | git checkout new_blanch
git checkout -b new_blanch
git merge some_blanch
git blanch -d deleted_branch
git mergetool
string for test itog
git push --set-upstream origin dev
git rm -r --cached .idea
git clone --branch=stepic https://github.com/Olhart/stepic_web_project.git web
git push origin --delete <branchName>
git ls-remote <remote>
