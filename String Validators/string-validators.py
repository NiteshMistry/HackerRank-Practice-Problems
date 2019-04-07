def string_validators(s):
    if(0<len(s)<1000):
        alphanumeric=alphabetical=digits=lowercase=uppercase = False 
        alphanumeric=any(i.isalnum() for i in s)
        alphabetical=any(i.isalpha() for i in s)
        digits=any(i.isdigit() for i in s)
        lowercase=any(i.islower() for i in s)
        uppercase=any(i.isupper() for i in s)
        return('%s\n%s\n%s\n%s\n%s'%(alphanumeric,alphabetical,digits,lowercase,uppercase))

if __name__ == '__main__':
    s = input()
    print(string_validators(s))