import re
# Task 1: Determine whether a string contains a ID number.


def has_id(string):
    # your code
    pattern = r"\w+:\s\d{6}-\d{2}-\d{4}"
    return bool(re.search(pattern, string))

    # Output
print(has_id("please don't share this: 890414-14-1422"))   # true
print(has_id("please confirm your identity: 234-122-1422"))  # false
# Task 2: Return the ID number from a string.


def grab_id(string):
    # your code
    pattern = r"(\d{6}-\d{2}-\d{4})"
    m = re.search(pattern, string)
    if m:
        return m.group(0)
    else:
        return "nil"

    # Output
print(grab_id("please don't share this: 890414-14-1422"))   # 890414-14-1422
print(grab_id("please confirm your identity: XXX-XX-1422"))  # nil
# Task 3: Return all of the ID numbers from a string.


def grab_all_ids(string):
    # your code
    pattern = r"\d{6}-\d{2}-\d{4}"
    return re.findall(pattern, string)

    # Output
    # ["890414-14-1422", "900515-14-1092", "950616-12-5414"]
print(grab_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
print(grab_all_ids("please confirm your identity: XXX-XX-1422"))  # []
# Task 4: Obfuscate all of the ID numbers in a string.

# Example: XXXX-XX-4430


def hide_all_ids(string):
    pattern = r"\d{6}-\d{2}-(\d{4})"
    return re.sub(pattern, r"XXXXXX-XX-\1", string)


    # XXXXXX-XX-1422, XXXXXX-XX-1092, XXXXXX-XX-5414
print(hide_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
# please confirm your identity: XXX-XX-1422
print(hide_all_ids("please confirm your identity: XXX-XX-1422"))


def format_ids(string):
    # Task 5: Ensure all of the ID numbers use * dashes for delimiters.*
    pattern = r"(\d{6})\.?(\d{2})\.?(\d{4})"
    return re.sub(pattern, r"\1-\2-\3", string)


    # 890414-14-1422, 900515-14-1092, 950616-12-5414
print(format_ids("890414.14.1422, 900515141092, 950616-12-5414"))
# please confirm your identity: 763158-58-1422
print(format_ids("please confirm your identity: 763158581422"))
