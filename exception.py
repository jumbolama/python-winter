while True:
    try:
        a=int(input('num'))
        b=int(input('arko num'))

        if b==5:
            raise Exception('5 number not accepted')
        print(a/b)

    except ZeroDivisionError:
        print('A number cannot div zero1')

    except Exception as e:
        print('something went wroong',e)    