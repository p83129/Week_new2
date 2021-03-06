def avg(data):
    count=data["count"]
    #print(count)
    sum=0
    for x in range(0,count):
        sum += data["employees"][x]["salary"]
    print((int)(sum/count))
    
 
    
avg({
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary":30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {   
                "name":"Jenny",
                "salary":50000
            }
        ]
})

