with open("nginx_logs.txt", "r", encoding="utf-8")as line:
    content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in line)
    for i in content:
        print(i)