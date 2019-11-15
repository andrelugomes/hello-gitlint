# Helo gitlint

+ http://jorisroovers.com/gitlint/

+ https://pre-commit.com/#intro


sudo apt-get install gitlint

gitlint --extra-path=custon_rules/

gitlint --config myconfigfile.ini    

cat commit-message | gitlint --config myconfigfile.ini 


## Hooks

gitlint install-hook  
pip install pre-commit 
pre-commit install --hook-type commit-msg

```
  ~/workspace/hello-gitlint |   master +8 !4 ····································
❯ git commit -m "commit without body"
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/andregomes/.cache/pre-commit/patch1573843897.
gitlint..................................................................Failed
hookid: gitlint

3: B6 Body message is missing

[INFO] Restored changes from /home/andregomes/.cache/pre-commit/patch1573843897.

```