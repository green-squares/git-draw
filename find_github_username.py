#!usr/bin/env python3

import requests
from itertools import product
from time import sleep
from threading import Thread
import os

def split_array(a, n):
    k, m = divmod(len(a), n)
    return [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

def exists(name):
    r = requests.get("https://github.com/" + name)
    return r.status_code != 404, r.status_code

alphabet = "abcdefghijklmnopqrstuvwxyz"


def permutations_of_n_letters(n):
    return [''.join(i) for i in product(alphabet, repeat = n)]

def worker(names, result, i):
    path = f"checked/_{i}.txt"
    # mine = open(path, "a")

    sleep(1)
    
    checked = []
    for p in os.listdir("./checked"):
        l = open("./checked/" + p, "r").readlines()
        for w in l:
            w = w.replace("\n", "")
            if w != "":
                checked.append(w)
                
    print(checked)
    
    good_names = []
    # sec = 0
    for name in names:
        if name in checked:
            continue
        mine = open(path, "a")
        mine.write("\n" + name)
        mine.close()
        e, s = exists(name)
        print(f"[Thread {i}] Name: {name} Exists: {e} Status: {s}")
        while s == 429:
            for sec in list(range(10))[::-1]:
                print(f"[Thread: {i}] Too many requests... waiting {sec} second(s)")
                sleep(1)
            e, s = exists(name)
            
        if s == 404: 
            good_names.append(name)
            mine = open(f"found/_{i}.txt", "a")
            mine.write("\n" + name)
            mine.close()
            
        # else:
        #     print(f"[Thread: {i}] Too many requests... waiting {sec} second(s)")
        #     sleep(1)
        #     sec -= 1
    result[i] = good_names
        
def start(perms, threads):
    parts = split_array(permutations_of_n_letters(perms), threads)
    threads = [None] * len(parts)
    results = [None] * len(parts)
    
    for i in range(len(parts)):
        threads[i] = Thread(target=worker, args=(parts[i], results, i))
        threads[i].start()
        
    for i in range(len(threads)):
        threads[i].join()
       
    print(results) 

if __name__ == '__main__':
    start(2, 10)
    
    
    
    