import pickle

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
            
    def importFromItemMan(itemMan):
        self.items = itemMan.loi
        print("Imported from loi.")

class itemManager():
    def __init__(self):
        print("Created an itemManager")
        self.loi = []
        self.identifier = "<=====>"
        self.listx = []
        
    def defineItem(self, name, iid):
        temp = name+self.identifier+str(iid)
        if temp not in self.loi:
            self.loi.append(temp)
            return True
        else:
            return False
        
    def getItem(self, iid=None, name=None):
        
        # This code is a mess
        # A big mess
        # Lots of bad loops that make no sense leftover
        # from the bad old system... but I guess that
        # it works! I'll redo this code sometime soon.
        # or not :)
        
        found = False
        indexValue = 0
        if name == None and not iid == None:
            while not found:
                found = True
                if indexValue > 1000:
                    return False
                else:
                    indexValue =+ 1
                x = self.loi
                for b in x:
                    b = b.split(self.identifier)
                    if str(b[1]) == str(iid):
                        return b[0]
            return False
        
        elif iid == None and not name == None:
            while not found:
                found = True
                if indexValue > 1000:
                    return False
                else:
                    indexValue =+ 1
                x = self.loi
                for b in x:
                    b = b.split(self.identifier)
                    if str(b[0]) == str(name):
                        return b[1]
            return False

        # Here true means that you tried to get the name / iid, while having both!
        # What is the point of using this function if you already have both xD
        
        return True

    def exportItems(self, file):
        with open(str(file)+'.pdata', 'wb') as f:
            pickle.dump(self.loi, f)

    def loadItems(self, file, listx):
        with open(str(file)+'.pdata', 'rb') as f:
            pickle.load(self.listx, f)

itemMan = itemManager()
itemMan.defineItem("Stone", 1)
itemMan.defineItem("Cheese", 2)
itemMan.defineItem("Rock", 3)
print(itemMan.getItem(3))
print(itemMan.getItem(2, "Cheese"))

itemMan.exportItems("ooOOoLaaLaa")
