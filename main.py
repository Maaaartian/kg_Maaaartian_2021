import sys

def solution(s, t):
    if not len(s) == len(t): return False # compare length of 2 strings
    map = {} # hash table to store intermediate mapping results
    for i in range(len(s)):
        # if a letter has appeared already and has been mapped to a new letter, return False
        if map.get(s[i]) and not map.get(s[i]) == t[i]: return False
        map[s[i]] = t[i] # update the hash table
    return True

if __name__ == '__main__':
    result = solution(sys.argv[1], sys.argv[2])
    print(result)