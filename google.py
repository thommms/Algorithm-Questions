def numUniqueEmails(email):
    res=[]
    at = 0
    plus=0
    sam=""
    for val in email:
      for i in val:
        if i == '@':
           at = 1
        if i == '+':
          plus = 1
        if i!='.' and at == 0 and plus == 0:
          sam+=i
        if at == 1:
          sam+=i
      for k in res:
        if
      res.append(sam)
      sam=""
      at = 0
      plus = 0

    print (res)
