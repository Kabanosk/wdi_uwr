## Package for Introduction to Computer Science at University of Wrocław. 
### Class Array provide:

- __init__(size1=0, size2=0, all_elements=0, rep=False, tab=None):
	- to create one-dimensional Array with zeros on each element set the size1 parameter to your size
	- to create two-dimensional Array with zeros on each element set the size1 and size2 parameters
	- if you change the all_elements parameter then Array will be filled with this value 
	- if set the rep to True value you will make Array with values form 0 to size1
	- you can also add tab as parameter, then items of the created Array will be this tab
 
- Operator overloading:
	- __setitem__(i, x) - setting the i-th element to x
	- __getitem__(i, x) - getting the i-th element
	- __len__() - for two-dimensional Array return tuple (size1, size2), for one-dimensional Array return size1

- other:
	- print() - printing Array in nice style

