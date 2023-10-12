def func(loopct,val):
    if loopct > 0:
        print(val)
        func(loopct - 1,val + 1)
    else:
        print("Function complete.")