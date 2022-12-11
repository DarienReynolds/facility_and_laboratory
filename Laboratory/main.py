class Laboratory:
    def __init__(self, labname, cost):
        self.labname = labname
        self.cost = cost

    def addlabtofile(self):
        newlabname = input("What is the name of the lab that you would like to add?")
        newlabcost = input("what is the cost of this new lab?")
        labfile = open("laboratories.txt", "a+")
        labfile.write("\n" + newlabname + "_" + newlabcost)
        labfile.close()

    def writelistoflabstofile(self):
        content = labhere.readlaboratoriesfile()
        labs_list = ('\n'.join(content))
        print(labs_list)
        labfile = open("laboratories.txt", "r+")
        labfile.write(labs_list)
        labfile.close()

    def displaylabslist(self):
        labs_list = labhere.readlaboratoriesfile()
        print(labs_list)

    def formatlabinfo(self, labname, cost):
        specificlab = (labname + "_" + cost)
        return specificlab

    def enterlaboratoryinfo(self):
        newlabname = input("What is the name of the lab that you would like to add?")
        newlabcost = input("what is the cost of this new lab?")
        newlab = labhere.formatlabinfo(newlabname, newlabcost)
        list = labhere.readlaboratoriesfile()
        list.append(newlab)

    def readlaboratoriesfile(self):
        labfile = open("laboratories.txt", "r")
        content = labfile.read()
        labs_list = content.split("\n")
        labfile.close()
        return labs_list


labhere = Laboratory("lab7", "1000")
labhere.displaylabslist()
