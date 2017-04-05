def is_in_newspaper(L, N):
   """
   >>> is_in_newspaper('hello', 'hello darkness my old friend')
   True
   >>> is_in_newspaper('hello', 'blablablabla')
   False
   """
   L_count = {}
   N_count = {}
   in_newspaper = True
   for letter in L:
      L_count[letter] = 1 + L_count.get(letter, 0)
      
   for letter in N:
      N_count[letter] = 1 + N_count.get(letter, 0)
   
   for key in L_count:
      if N_count.get(key) < L_count.get(key):
         in_newspaper = False

   return in_newspaper

if __name__ == "__main__":
   import doctest
   results = doctest.testmod()
   if results.failed == 0:
      print "ALL TESTS PASSED!"
         