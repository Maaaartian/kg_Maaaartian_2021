import sys

def solution(s, t):
    if not len(s) == len(t): return False
    map = {}
    for i in range(len(s)):
        if map.get(s[i]) and not map.get(s[i]) == t[i]: return False
        map[s[i]] = t[i]
    return True

if __name__ == '__main__':
    result = solution(sys.argv[1], sys.argv[2])
    print(result)