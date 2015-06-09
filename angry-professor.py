def on_time(t, b):
    count = 0
    for i in t:
        if i <= 0:
            count += 1
    if count >= b:
        print "NO"
    else:
        print "YES"


test_cases = int(raw_input().strip())

for _ in range(test_cases):
    n,k = [int(x) for x in raw_input().strip().split()]
    times = [int(x) for x in raw_input().strip().split()]
    on_time(times,k)
