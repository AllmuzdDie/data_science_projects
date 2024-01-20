
def dummy(x):
    return f"Эта функция ничего не вызывает {x}"
    
def dummy_2(y):
    return dummy(y) + "dummy_2"
    
print(dummy_2("кошка"))