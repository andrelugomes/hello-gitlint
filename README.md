# Helo gitlint

+ http://jorisroovers.com/gitlint/

+ https://pre-commit.com/#intro

```
sudo apt-get install gitlint
```
## Custon rules

```
gitlint --extra-path=custon_rules
```

## Configuring current rules
Set up --extra-path inside `myconfigfile.ini`

```
extra-path=custon_rules/
```
Run
```
gitlint --config myconfigfile.ini   
```

### Good commit message

```
cat good-commit-message | gitlint --config myconfigfile.ini 
```

### Bad commits

```
echo "This is a bad commit message" | gitlint --config myconfigfile.ini 


cat bad-commit-message | gitlint --config myconfigfile.ini 
```

## Hooks

```bash
gitlint install-hook  

pip install pre-commit gitlint

pre-commit install --hook-type commit-msg
```

```text
  ~/workspace/hello-gitlint |   master +8 !4 ····································
❯ git commit -m "commit without body"
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/andregomes/.cache/pre-commit/patch1573843897.
gitlint..................................................................Failed
hookid: gitlint

3: B6 Body message is missing

[INFO] Restored changes from /home/andregomes/.cache/pre-commit/patch1573843897.

```
