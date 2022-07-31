#!/bin/bash
tmux new -d -s main
tmux send-keys -t main "python3 ./ducksquad.py" ENTER
tmux a -t main
