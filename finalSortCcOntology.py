import pandas as pd
import numpy as np
import collections
import itertools
import matplotlib.pyplot as plt
import numpy
import re


import seaborn as sns

def main(): # s# Final adjustments for the sorted CC ontology: ① Remove 'None'. ② Since there are unsorted CC terms, reorder them. for GitHub

  sortedOnto = pd.read_csv("/YourPath/conceptCafeOntologySorted.txt", sep="\t")

  noIdLev1 = list(sortedOnto[sortedOnto.ccTerm=="なし"].CCID)[0][0:4]
  print(noIdLev1)


  sortedOnto = sortedOnto[~sortedOnto.CCID.str.contains(noIdLev1)]

  allLev1s = []

  #outF = open("/YourPath/conceptCafeOntologySortedLas.txt", "w")
  outF = "/YourPath/conceptCafeOntologySortedLas.txt"


  #sortedOntoV2 = sortedOnto
  idV2D = []
  for index, row in sortedOnto.iterrows():
    curLv1 = row[0][2] + row[0][3]  # Get the position of Level1
    curLv1af = 0  # This is for inserting the corrected CC terms of other groups after excluding the 'なし' CC term group.

    resId = row[0]  # for saving

    # print("noIdLev1")
    # print(noIdLev1)
    # print(list(noIdLev1)[2])
    # print(list(noIdLev1[3]))
    # print(list(noIdLev1)[2]+list(noIdLev1[3]))

    #print("int(curLv1) > int(list(noIdLev1)[2]+list(noIdLev1)[3]):")
    #print(int(curLv1))
    #print(int(list(noIdLev1)[2]+list(noIdLev1)[3]))
    #print("-")

    if int(curLv1) > int(list(noIdLev1)[2]+list(noIdLev1)[3]): # For example, when Lv.16 > Lv.15, subtract 1 from int(curLv1) to get CC15.

    #CC15
    #noIdLev1
    #CC15
    #1
    #['5']

    #TypeError: can only concatenate str (not "list") to str

      curLv1af = int(curLv1) - 1
      #curLv1af = str(curLv1af)
      if int(curLv1af) < 10:
        curLv1af = "0" + str(curLv1af)

        resIdsp = list(resId)
        resIdsp[2] = list(curLv1af)[0]
        resIdsp[3] = list(curLv1af)[1]
        resId = "".join(resIdsp)
        #list(resId)[2] = list(curLv1af)[0]
        #list(resId)[3] = list(curLv1af)[1]
        idV2D.append(resId)

      else:
        curLv1af = str(curLv1af)
        #resId = row[0]
        resIdsp = list(resId)
        resIdsp[2] = list(curLv1af)[0]
        resIdsp[3] = list(curLv1af)[1]
        resId = "".join(resIdsp)
        #list(resId)[2] = list(curLv1af)[0]
        #list(resId)[3] = list(curLv1af)[1]
        idV2D.append(resId)
    else:
      idV2D.append(resId)

  sortedOntoV2 = pd.DataFrame(
    data = {
            'CCID' : idV2D,
            'ccTerm' : list(sortedOnto.ccTerm)
          }
  )

  #np.set_printoptions(np.inf)
  #numpy.set_printoptions(numpy.inf)
  pd.set_option('display.max_rows', None)
  sortedOntoV2 = sortedOntoV2.sort_values('CCID')
  print(sortedOntoV2)

  sortedOntoV2.to_csv(outF, sep="\t", index=False)

 

if __name__ == "__main__":
    main()
