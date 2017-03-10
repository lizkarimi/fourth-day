class List_Class(object):

	def __init__(self, Len_of_list_to_create, diff_btw_cons_numbers):
		self.start = diff_btw_cons_numbers
		self.size = Len_of_list_to_create
		self.variablelength = len(range(self.start,self.size,self.start))

	def getSize(self):
	 	return self.variablelength 

class BinarySearch(List_Class):
	"""docstring for BinarySearch"""
	def __init__(self, Stop, Start):
		self.Start = Start
		self.Stop = Stop + 1
		self.length = List_Class(self.Start, self.Stop ).getSize()
	
	def Test(self):
		return self.length


	def search(self, Number):
		List = self.Create(self.Start, self.Stop*self.Start)

		self.count = self.Search(List, List, Number, 1)
		
		return self.count

	def Search(self,List, Original, Number, Count = 1):
		self.List = List
		self.Original = Original
		self.Number = Number
		self.Count = Count

		if len(self.List) % 2 != 1:
			self.List.insert(0, 0)

		if len(self.List) == 3 :
			if self.List[0] == self.Number:
				return "Count :",self.Count, " Index :",self.Original.index(self.Number)-1

			elif self.List[1] == self.Number:
				return "Count :",self.Count, " Index :",self.Original.index(self.Number)-1	
			
			elif self.List[2] == self.Number:
				return "Count :",self.Count, " Index :",self.Original.index(self.Number)-1	
			
			else:
				return "Count :",self.Count/2+1 , " Index :",-1	

		elif List[0] == Number:
			return "Count :",self.Count+1, " Index :",self.Original.index(self.Number)-1

		elif len(self.List) == 1:
			if List[0] == Number:
				return "Count :",self.Count+2, " Index :",self.Original.index(self.Number)-1
			else:
				return "count :",self.Count/2 +1, " Index :",-1	

		elif self.List[len(List)-1] == self.Number:
				return "Count :",0, " Index :",self.Original.index(self.Number)-1	

		else:
				
			if self.List[(len(self.List))/2] > self.Number:
				self.List = self.List[0 : (len(self.List))/2]
				
				return self.Search(self.List, self.Original, self.Number, self.Count+1)

			elif self.List[(len(self.List))/2] < self.Number:
				self.List = self.List[(len(self.List)+1)/2 : len(self.List)]
				return self.Search(self.List, self.Original, self.Number, self.Count+1)

			elif self.List[(len(self.List))/2] == self.Number:
				
				return "Count :",self.Count+2, " Index :",self.Original.index(self.Number)-1

	def Create(self,start,stop):
		print " "
		List = []
		for x in range(start, stop, start):
			List.append(x)

		return List		



