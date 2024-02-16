number = set(range(1, 10001))
non_self = set()
for num in number:
    for n in str(num):
        num += int(n)
    non_self.add(num)

self_num=number - non_self
for self_n in sorted(self_num):
    print(self_n)
