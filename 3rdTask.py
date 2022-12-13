class MyList(list):
    def __init__(self,list):
        self.lst = list
        print("работает магический метод")

    def __str__(self):
        print("работает магический метод")
        return f"{self.lst}"

    def __len__(self):
        print("работает магический метод")
        return len(self.lst)

    def __getitem__(self, item):
        print("работает магический метод")
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value
        print("работает магический метод")

lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))