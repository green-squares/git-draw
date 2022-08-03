#!/usr/bin/env python3

# Justus Languell 2022

user = "green-squares"
pat = "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"
repo = "git-draw"

def push(username, password, user, repo):
    return f"git push https://'{username}':'{password}'@github.com/{user}/{repo}.git"

def commit(username, password, repo):

print(push(user, pat, user, repo))

