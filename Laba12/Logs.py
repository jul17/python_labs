import re

if __name__ == "__main__":
    count = 0
    with open("access_log") as file:
        for line in file:
            if re.search('09/Mar/2004:2[1-3]:[1-5][0-9]:[0-5][0-9] ',
                         str(line))or re.search('10/Mar/2004',str(line)) or re.search('11/Mar/2004:[0-1][0-9]:[1-2][0-9]:[0-2][0-8]',str(line)):
                count += 1

print("The number of requests for each status in the interval:...", count)