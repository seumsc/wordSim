class dict:
    def __init__(self):
        pass

    def data(self):
        file=open("dict.txt")
        list=[]
        try:
            # list=file.readlines()
            for i in file:
                i=i.strip('\n')
                list.append(i)
        finally:
            file.close()
        # for i in list:
        #     i=i.strip('\n')
        # print(list)
        # print(len(list))
        return list

if __name__=='__main__':
    exp=dict()
    exp.data()