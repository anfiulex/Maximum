def palindrom(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False
print(palindrom('лепсспел'))
print(palindrom('helloworld'))
