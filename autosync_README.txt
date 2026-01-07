cat > autosync_info.txt << 'EOF'
==============================
      AUTOSYNC CONTROL GUIDE
==============================

Autosync runs in background and automatically:
git add .
git commit
git push

Use these controls when doing advanced Git work.


--------------------------------
CHECK IF AUTOSYNC IS RUNNING
--------------------------------
ps aux | grep autosync


--------------------------------
PAUSE AUTOSYNC (TEMPORARY)
--------------------------------
pkill -f autosync.sh

Use when:
- Switching branches
- Rebasing
- Resetting commits
- Fixing merge conflicts
- Editing commit history
- Cleaning large file changes


--------------------------------
RESTART AUTOSYNC
--------------------------------
~/.autosync.sh &

Use after finishing advanced Git operations.


--------------------------------
STOP AUTOSYNC COMPLETELY (MANUAL MODE)
--------------------------------
pkill -f autosync.sh
Remove autosync from bashrc:
nano ~/.bashrc
(delete autosync block)

Use when:
- You want manual Git control
- Working on sensitive repos
- Pushing selective commits only


--------------------------------
VISUAL FLOW
--------------------------------
Heavy Git Work → pkill -f autosync.sh
Finish work → ~/.autosync.sh &
Return to automatic safe mode


Autosync is your assistant.
You are the engineer.
EOF

