def pw():
    import random
    pas2 = list('ABCDEFGHIGKLMNopqrstuvyxwz123456')
    pas3 = list('abcdefghigklmnOPQRSTUVYXWZ7890')
    random.shuffle(pas2)
    random.shuffle(pas3)
    passwd = 'WN_' + ''.join([random.choice(pas2) for x in range(11)] + [random.choice(pas3) for x in range(11)])
    return passwd



