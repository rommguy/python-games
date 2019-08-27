a = 'G'
b = 'u'
c = 'y'


# function definition
def check_is_guy(str):
    is_guy = str == 'Guy'
    if is_guy:
        return "This is Guy"
    else:
        return "This is not Guy"


# run the functions
print check_is_guy("bla bla")
print check_is_guy(a + b + c)
