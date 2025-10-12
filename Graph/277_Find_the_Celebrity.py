def find_the_celebrity(x):
    n = len(x)

    # find the 候選rows of celebrity
    for r in range(n):
        if sum(x[r]) == 1:
            canditate = r
    # check columns(其他人認識他)
            for c in range(n):
               if c != canditate and x[c][canditate] != 1:
                   return 0
            return canditate + 1 
        return 0 #沒人是canditate

x = [
  [1, 0, 0],
  [1, 1, 0],
  [1, 1, 1]
]
print(find_the_celebrity(x))