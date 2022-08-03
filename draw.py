#!/usr/bin/env python3

# Justus Languell 2022

import random
import hashlib
import subprocess
import os


USERNAME = "green-squares"
EMAIL = "justin889103@gmail.com"
PERSONAL_ACCESS_TOKEN = "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"
REPO = "git-draw"

class Git:
    def __init__(self, username, email, personal_access_token, repo_owner, repo_name):
        self.username = username
        self.email = email
        self.personal_access_token = personal_access_token
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        
    def add(self):
        os.system(f"git add .")
    
    def commit(self, date, message):
        os.system(f'GIT_COMMITTER_NAME="{self.username}" GIT_COMMITTER_EMAIL="{self.email}" git commit --author="green-squares <{self.email}>" -a -m "{message}"')

    def push(self):
        os.system(f"git push https://'{self.username}':'{self.personal_access_token}'@github.com/{self.repo_owner}/{self.repo_name}.git")
        print(f"git push https://'{self.username}':'{self.personal_access_token}'@github.com/{self.repo_owner}/{self.repo_name}.git")
    
def write_random_data():
    s = hashlib.sha256(bytes(str(random.randint(1e5, 1e6 - 1)),'utf-8')).hexdigest()
    open("random.txt", "a").write(s + "\n")
    return s

if __name__ == "__main__":
    git = Git(USERNAME, EMAIL, PERSONAL_ACCESS_TOKEN, USERNAME, REPO)

    s = write_random_data()
    git.add()
    git.commit(None, s)
    git.push()
