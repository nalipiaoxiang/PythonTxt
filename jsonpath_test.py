from jsonpath import jsonpath


#常规
date = {'key1':{'key2':{'key3':{'key4':{'key5':{'key6':'python'}}}}}}
print(date['key1']['key2']['key3']['key4']['key5']['key6'])

print(jsonpath(date,'$.key1.key2.key3.key4.key5.key6')[0])
print(jsonpath(date,'$..key6')[0])