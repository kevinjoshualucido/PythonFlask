def best_friend(txt,a,b):
    return txt.count(a)==txt.count(a+b)


print(best_friend("this is a test", "i", "s"))
print(best_friend("abcdee", "e", "e"))