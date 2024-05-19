try:
    1/0
except:
    print("This is error")


#### Handling multiple Errors in sequence"
try:
    #1/0
    print(xyz)
except ZeroDivisionError:
    print("This is ZeroDivisionError handled")
except NameError:
    print("This is name error")

#### multiple Errors in same code block as below"

try:
    #1/0
    print(xyz)
except (ZeroDivisionError,NameError):     #Notice paranthesis and , ;
    print("This is both erros handled")


temp=1
try:
    assert temp==2
except AssertionError:
    print("Assertion Error is present????")
