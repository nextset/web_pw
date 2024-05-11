def pw():
    import random
    pas1 = list('ABCDEFGHIGKLMNopqrstuvyxwz123456')
    pas1 = list('abcdefghigklmnOPQRSTUVYXWZ7890')
    random.shuffle(pas2)
    random.shuffle(pas3)
    passwd = 'WN_' + ''.join([random.choice(pas1) for x in range(11)] + [random.choice(pas2) for x in range(11)])
    return passwd



