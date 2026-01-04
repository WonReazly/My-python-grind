num = int(input())
string = []
for _ in range(num):
    string.append(input())
k = int(input())
zapr = []
for _ in range(k):
    zapr.append(input())
for s in string:
    s_lower = s.lower()
    all_found = True
    
    for q in zapr:
        if q.lower() not in s_lower:
            all_found = False
            break
    if all_found:
        print(s)
