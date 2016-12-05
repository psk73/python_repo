import sys
def getObjectInfo(obj,spacing=10,collapse=1):
  """
  Finds the callable methods of the object and prints them.
  `"""
  methodList = [method for method in dir(obj) if callable(getattr(obj,method))]
  processFunction = collapse and (lambda s: "".join(s.split())) or (lambda s:s)

  print "\n". join(["%s %s" % 
                     (method.ljust(spacing),  
		      processFunction(str(getattr(obj,method).__doc__)))
		      for method in methodList])

  return


def main():
  ob = sys.argv[1]

  if sys.argv[1] == "int":
    ob = 1

  if sys.argv[1] == "float":
    ob = 1.0

  if sys.argv[1] == "list":
    ob = []
  
  if sys.argv[1] == "string":
    ob = " "

  if sys.argv[1] == "dict":
    ob = {}
  
  getObjectInfo( ob )
  return


if __name__ == "__main__":
  main()

