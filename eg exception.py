while True:
    try:


        array=[1,3,5,8,9]

        a=int(input('enter number'))
        print(array[a])

        if a<len(array):
          raise Exception('array not found')
        print(array[a])

    except Exception as e:
       print('erroe',e)