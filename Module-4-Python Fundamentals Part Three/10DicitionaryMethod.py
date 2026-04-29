
info ={
    "name":"alvinsifat", 
    "cgpa":9.2,
    "subjects":["math", "science"]
}
# sob gular key chole ashbe 
print(info.keys())

# convart to key 
dici_key = list(info.keys())
print(dici_key)
print(type(dici_key))


# bitor value gulo chole ashbe 
print(info.values())
# list er bitor a items gulo chole ashbe['math', 'science']"
print(info.items())
print(info.get("cgpa"))

info.update({
    "name":"akash"
})
print(info)