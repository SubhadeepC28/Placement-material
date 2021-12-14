def process(file,t,r):
    with open(file,"w") as f:
        for i in zip(t,r[::-1]):
            f.write(i[0]+" "+i[1]+"\n")
    f=open(file,"w")
    f.write("{} {} and can also be used {}".format(t[-3],r[0],r[-2]))
    f.close()
    try:
        with open(file) as f:
            f.seek(1,1)
            print(f.read(6))
    except IOError:
        print('Error Processing file')
if __name__ == '__main__':
    t=["Py","Js","Go"]
    r=["works best", "for web dev", "stat typed"]
    process("myfile.txt",t,r)