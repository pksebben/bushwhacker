# Bushwhacker

This is a set of tools to assist in the examination and grokking of
code.  It is meant to be installed in a user's site-packages, and
imported when needed to inspect objects, print isolated stack traces,
and generally 'get a sense' of what code is doing.


# Usage

Install or symlink into your user site-packages directory.

In the module you're working on, import like:

`from bushwhacker.bushwhacker import *`

this imports a series of functions that can be used as follows:

## Object inspection

object inspection works on anything you feed it; lists, dicts,
objects, functions.  It prints out a list of all the 'stuff' in the
'thing'.

It's ouput is very verbose.

```python
thing = Thing() # thing	we want to know more about

o.inspect(thing)
```
...when run, this will print to stdout something looking like:
```
__add__ :: <method-wrapper '__add__' of list object at 0x100b39cc0>
__class__ :: <class 'list'>
__class_getitem__ :: <built-in method __class_getitem__ of type object at 0x1008efab0>
__contains__ :: <method-wrapper '__contains__' of list object at 0x100b39cc0>
__delattr__ :: <method-wrapper '__delattr__' of list object at 0x100b39cc0>
__delitem__ :: <method-wrapper '__delitem__' of list object at 0x100b39cc0>
__dir__ :: <built-in method __dir__ of list object at 0x100b39cc0>
__doc__ :: Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
__eq__ :: <method-wrapper '__eq__' of list object at 0x100b39cc0>
__format__ :: <built-in method __format__ of list object at 0x100b39cc0>
__ge__ :: <method-wrapper '__ge__' of list object at 0x100b39cc0>
__getattribute__ :: <method-wrapper '__getattribute__' of list object at 0x100b39cc0>
__getitem__ :: <built-in method __getitem__ of list object at 0x100b39cc0>
__gt__ :: <method-wrapper '__gt__' of list object at 0x100b39cc0>
__hash__ :: None
__iadd__ :: <method-wrapper '__iadd__' of list object at 0x100b39cc0>
__imul__ :: <method-wrapper '__imul__' of list object at 0x100b39cc0>
__init__ :: <method-wrapper '__init__' of list object at 0x100b39cc0>
__init_subclass__ :: <built-in method __init_subclass__ of type object at 0x1008efab0>
__iter__ :: <method-wrapper '__iter__' of list object at 0x100b39cc0>
__le__ :: <method-wrapper '__le__' of list object at 0x100b39cc0>
__len__ :: <method-wrapper '__len__' of list object at 0x100b39cc0>
__lt__ :: <method-wrapper '__lt__' of list object at 0x100b39cc0>
__mul__ :: <method-wrapper '__mul__' of list object at 0x100b39cc0>
__ne__ :: <method-wrapper '__ne__' of list object at 0x100b39cc0>
__new__ :: <built-in method __new__ of type object at 0x1008efab0>
__reduce__ :: <built-in method __reduce__ of list object at 0x100b39cc0>
__reduce_ex__ :: <built-in method __reduce_ex__ of list object at 0x100b39cc0>
__repr__ :: <method-wrapper '__repr__' of list object at 0x100b39cc0>
__reversed__ :: <built-in method __reversed__ of list object at 0x100b39cc0>
__rmul__ :: <method-wrapper '__rmul__' of list object at 0x100b39cc0>
__setattr__ :: <method-wrapper '__setattr__' of list object at 0x100b39cc0>
__setitem__ :: <method-wrapper '__setitem__' of list object at 0x100b39cc0>
__sizeof__ :: <built-in method __sizeof__ of list object at 0x100b39cc0>
__str__ :: <method-wrapper '__str__' of list object at 0x100b39cc0>
__subclasshook__ :: <built-in method __subclasshook__ of type object at 0x1008efab0>
append :: <built-in method append of list object at 0x100b39cc0>
clear :: <built-in method clear of list object at 0x100b39cc0>
copy :: <built-in method copy of list object at 0x100b39cc0>
count :: <built-in method count of list object at 0x100b39cc0>
extend :: <built-in method extend of list object at 0x100b39cc0>
index :: <built-in method index of list object at 0x100b39cc0>
insert :: <built-in method insert of list object at 0x100b39cc0>
pop :: <built-in method pop of list object at 0x100b39cc0>
remove :: <built-in method remove of list object at 0x100b39cc0>
reverse :: <built-in method reverse of list object at 0x100b39cc0>
sort :: <built-in method sort of list object at 0x100b39cc0>
ITEM: el1
ITEM: el2
ITEM: el3
not a dict
```

# Roadmap

 - object inspection
   - for i in dir: print xx.....
	 - verbosity controls
 - stack tracing
   - print stack trace isolated to:
	 - x package
	 - x module
	 - anything not 3rd party
	 - anything related to:
		 - a particular function
		 - a particular variable
 - object tracing
   - value tracking
 - namespace tooling
   - print things in namespace (reduced to be useful)
 - configuration
