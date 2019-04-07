def count_substring(s, ss):
    count = 0
    for i in range(0, len(s)):
        if (s[i] == ss[0]):
            for j in range(0, len(ss)):
                if (i + j < len(s)):
                    if (s[i + j] != ss[j]):
                        break
                    if (s[i + j] == ss[j] and j == len(ss) - 1):
                        count += 1
    return (count)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)