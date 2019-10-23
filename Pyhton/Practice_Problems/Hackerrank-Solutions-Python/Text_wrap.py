def wrap(string, max_width):
    c=0
    p=''
    for i in string:
        if c==(max_width-1):
            p+=(i+'\n')
            c=0
        else:
            p+=i
            c+=1

    return p

