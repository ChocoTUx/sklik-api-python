import fileinput, re
import glob

'''
Anonymyzer    
Setup all config variables to default and replace IDs to default value 123456
'''
for filename in glob.glob('./../qrs/*.py'):
    if filename == "anonymizer.py":
        continue
    print(filename)
    for line in fileinput.input([filename], inplace=True):
        if re.search(r"get_logged_user_struct\('[a-zA-Z0-9]*'\)", line) is not None:
            print(re.sub(r"get_logged_user_struct\('[a-zA-Z0-9]*'\)", "get_logged_user_struct('default')", line), end='')

        elif re.search(r"Root\('([a-z]*)'\,\s*'([a-z]*)'\)", line) is not None:
            print(re.sub(r"Root\('([a-z]*)'\,\s*'([a-z]*)'\)", r"Root('\1', 'default')", line), end='')

        elif re.search(r"'([a-zA-Z]*(Id|id))':\s*[0-9]*", line) is not None:
            print(re.sub(r"'([a-zA-Z]*(Id|id))':\s*[0-9]*", r"'\1': 123456", line), end='')

        elif re.search(r"'([a-zA-Z]*(Ids|ids))':\s*\[[0-9,\s]*\]", line) is not None:
            print(re.sub(r"'([a-zA-Z]*(Ids|ids))':\s*\[[0-9,\s]*\]", r"'\1': [123456]", line), end='')  

        else:
            print(line, end='')

