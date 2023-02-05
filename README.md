# Bushwhacker

This is a set of tools to assist in the examination and grokking of
code.  It is meant to be installed in a user's site-packages, and
imported when needed to inspect objects, print isolated stack traces,
and generally 'get a sense' of what code is doing.


# Roadmap

 - object inspection
   - for i in dir: print xx.....
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
