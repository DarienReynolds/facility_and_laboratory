class Facility:
    def __init__(self, Facility_Name):
        self.facilityName = Facility_Name

    def addFacility(self):
        newfacilityname = self.facilityName
        facilityfile = open("facilities.txt", "a+")
        facilityfile.write("\n" + newfacilityname)
        facilityfile.close()

    def displayFacilities(self):
        facility_list = facilityone.makeListOfFacilities()
        print(facility_list)

    def writeListOfFacilitiesToFile(self):
        content = facilityone.makeListOfFacilities()
        facilities_list = ('\n'.join(content))
        print(facilities_list)
        faciltyfile = open("facilities.txt", "r+")
        faciltyfile.write(facilities_list)
        faciltyfile.close()

    def makeListOfFacilities(self):
        facilityfile = open("facilities.txt", "r")
        content = facilityfile.read()
        facility_list = content.split("\n")
        facilityfile.close()
        return facility_list

facilityone = Facility("Fire")
