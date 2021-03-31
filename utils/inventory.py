import json

class inventoryManager():
    def __init__(self):
        self.items = []

    def addItem(self, item):
        if item not in self.items:
            self.items.append(item)

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)

    def getItems(self):
        return self.items

    def setItem(self, index, item):
        if len(self.items) > int(index):
            self.items[int(index)] = item

    def mergeList(self, listToMerge):
        self.items += listToMerge

    def unmergeList(self, listToUnmerge):
        for item in listToUnmerge:
            try:
                self.items.remove(item)
            except Exception:
                pass

class itemManager():
    def __init__(self):
        print("Created an itemManager")
        self.loi = []
        self.identifier = "<=====>"
        
    def defineItem(self, name, iid):
        temp = name+self.identifier+iid
        if temp not in self.loi:
            self.loi.append(temp)
            return True
        else:
            return False
        
    def getItem(self, iid=None, name=None):
        
        # This code is a mess
        # A big mess
        
        found = False
        indexValue = 0
        if name == None and not iid == None:
            while not found:
                if indexValue > 1000:
                    return False
                else:
                    indexValue =+ 1
                x = self.loi
                if x[1] == iid:
                    return x[0] 
            return False
        
        elif iid == None and not name == None:
            while not found:
                if indexValue > 1000:
                    return False
                else:
                    indexValue =+ 1
                x = self.loi
                if x[0] == name:
                    return x[1] 
            return False

        # Here true means that you tried to get the name / iid, while having both!
        # What is the point of using this function if you already have both xD
        
        return True

    def exportItems(self, file):
        with open(str(file)+'.json', 'w') as f:
            json.dump(self.loi, f)
