def ckeck(ans):
    if int(ans.strip()) == 0 or int(ans.strip() == 1):
        return True
    else:
        print('Некорекктный ввод. Повторите снова')
        print()
        return False