import pandas as pd
import numpy as np
import collections
import itertools
import matplotlib.pyplot as plt
import numpy as np
import re


import seaborn as sns

def main(): # Sort the CC ontology in alphabetical order (gojūon order) for GitHub


  ccOntology = pd.read_csv("/YourPath/conceptCafeOntology.txt", sep="\t")

  curOntoD = pd.DataFrame(
      data = {
            'CCID' : [],
            'ccTerm' : []
          }
        )

  #outF =
  outF = open("/YourPath/conceptCafeOntologySorted.txt", "w")
  outF.write("CCID" + "\t" + "ccTerm" + "\n")

  for i in range(1,44):
    #print(i)
    if i < 10:
      curLev1 = "0" + str(i)
    else:
      curLev1 = str(i)

    #curOntoD = []
    curOntoD = pd.DataFrame(
          data = {
            'CCID' : [],
            'ccTerm' : []
          }
      )
    for indexJ, rowJ in ccOntology.iterrows():
      # tmpOntD = pd.DataFrame(
      #     data = {
      #       'CCID' : [],
      #       'ccTErm' : []
      #     }
      # )

      #print("str(list(rowJ[0])[2:3])")
      #print(rowJ[0])
      parCCid = (list(rowJ[0]))[2] + (list(rowJ[0]))[3]

      #print(curLev1)
      #print("----")
      if parCCid == curLev1:  # If it is an arbitrary Level 1 CC term.
        #print(str(list(rowJ[0])[2:3]))
        #print(curLev1)
        #print("-----")
        tmpOntD = pd.DataFrame(
          data = {
            'CCID' : [rowJ[0]],
            'ccTerm' : [rowJ[1]]
          }
        )

        curOntoD = pd.concat([curOntoD, tmpOntD])
    #print("Display one element from Level 1 and beyond（例：CC term of 職業 ）")
    #print(curOntoD)
    #break


    #tmpLev1 = curOntoD.sort_values('ccTerm')

    #tmpIdLev1 = curOntoD.CCID
    #print(list(tmpIdLev1))
    #print(tmpLev1)
    tmpLev2D = pd.DataFrame(
      data = {
        'CCID' : [],
          'ccTerm' : []
        }
     )
    topF = 0
    for indexK, rowK in curOntoD.iterrows():
      if topF == 0:
        #print(str(indexK) + "  " + rowK[0] + " " + rowK[1])
        outF.write(rowK[0] + "\t" + rowK[1] + "\n") # List the Level 1 CC terms
        print(rowK[0] + " " + rowK[1] + " " + "Level1")
        #break
      topF = 1



      #curOntoD = pd.concat([curOntoD, tmpOntD])
      #print(rowK[0])
      #print("".join(list(rowK[0])[5:9]))
      #print(list(rowK[0]))
      # print("rowK[0]")
      # print(rowK[0])
      # print("(list(rowK[0])[5:9]) == 0000")
      # print("".join(list(rowK[0])[5:9]))
      # print("list(rowK[0])[4] != 0:")
      # print(list(rowK[0])[4])

      if "".join(list(rowK[0])[5:9]) == "0000" and list(rowK[0])[4] != "0":
        #print(rowK[0])
        tmpLev2D = pd.concat([tmpLev2D, pd.DataFrame(data={'CCID' : [rowK[0]], 'ccTerm' : [rowK[1]]})])

      #CC0110000 is モデル

    #print("Level2のcc terms")
    #print(tmpLev2D) # Get any Level2 CC term（CCID，ccTerm
    x = list(tmpLev2D.CCID)
    tmpLev2Daf = tmpLev2D.sort_values("ccTerm")
    tmpLev2Daf.CCID = x
    #print("After arranging Level2 CC terms")
    #print(tmpLev2Daf)


    #break

    print("tmpLev2D tmpLev2D tmpLev2D")
    print(tmpLev2D)

    print("tmpLev2Daf tmpLev2Daf tmpLev2Daf")
    print(tmpLev2Daf)


    for indexL, rowL in tmpLev2Daf.iterrows():

      outF.write(rowL[0] + "\t" + rowL[1] + "\n")
      print(rowL[0] + " " + rowL[1]  + " " + "Level2")

      curD = tmpLev2D[tmpLev2D.ccTerm == rowL[1]] # Track back to the original CC term
      #print(curD)
      # What is the valuable "tmpLev2D"? → any Level2 CC term
      # What is the valuable "curOntoD"? → lower than Level1 any CC term is put



      #print(list(curD.CCID))

      #tmpLev3id = list(curD.CCID)[5]




      #print("CC01w")

      tmpTarTerm = list(curD.CCID)[0][0:5]  # CC01i0000 → CC01i     CC01f0000 →　CC01f

      tmpLev3 = curOntoD[curOntoD.CCID.str.contains(tmpTarTerm)]  # Less than Level3 CC terms

      # nowTmpD = []
      # for tL3 in tmpLev3:
      #   if list(tL3)[6] == "0": # If Level4 is zero
      #     nowTmpD.append(tL3)
      # tmpLev3 = nowTmpD


      tmpLev3id = list(tmpLev3.CCID)
      #print("tmpLev3id.remove(curD.CCID[0])")
      #print(curD.CCID[0])
      #tmpLev3id
      tmpLev3id.remove(curD.CCID[0])  # Exclude this due to the existence of Level2 CC terms

      tmpLev3idTmp = []
      for tL3 in tmpLev3id: # Judge if there is any Level3 and higher CC terms
        if list(tL3)[6] != "0": #CC01f1"0"00 と #CC01f1"1"00
        #if list(tL3)[6] == "0": #CC01f1"0"00 と #CC01f1"1"00    # Keep only Level 3
          tmpLev3idTmp.append(tL3)                               # Keep Level 4 or more CC terms

      #tmpLev3id

      print("tmpLev3 = curOntoD[curOntoD.CCID.str.contains(tmpTarTerm)]")
      print("curOntoD.CCID")
      print(curOntoD.CCID)
      print("tmpTarTerm") # CC01i # Only up to Level2 CC terms are shown
      print(tmpTarTerm) # CC01f...
      print("tmpLev3")
      print(tmpLev3)
      print("tmpLev3id")
      print(tmpLev3id)


      #tmpLev4id = list(curOntoD[curOntoD.CCID.str.contains("".join(tmpTarId4))].CCID)
      #tmpLev4id.remove(rowM[0])

      #nowTmpD = []
      nowTmpDall = pd.DataFrame({
            'CCID' : [],
            'ccTerm' : []
      })
      for index, tL3 in tmpLev3.iterrows():
        if list(tL3[0])[5] != "0" and list(tL3[0])[6] == "0": # If Level3 number is not zero and Level4 number is zero（because it is prefereble to sort only Lv.3 CC terms）

          #print(nowTmpD)
          nowTmpD = pd.DataFrame(
              data = {
                  'CCID' : [tL3[0]],
                  'ccTerm' : [tL3[1]]
              }
          )
          #print("nowTmpD = pd.DataFrame(")
          #print(nowTmpD)
          nowTmpDall = pd.concat([nowTmpDall, nowTmpD])
          #nowTmpD.append(tL3)
      tmpLev3 = nowTmpDall
      print("tmpLev3 = nowTmpDall  This is only Level3 and the lower terms")
      print(tmpLev3)


      #tmpLev3 = tmpLev3[tmpLev3.CCID.isin(tmpLev3id)]
      # "tmpLEv3id" is CC terms except level2 (Exclude CC terms of 学生，女子大生，女子大生の場合は，学生)


      #print()
      #print(tmpLev3)
      #print(tmpLev3id)


      #if tmpLev3id == list(curD.CCID):
      #  tmpLev3id = []
      #print("tmpLev3id tmpLev3id tmpLev3id")
      #print(tmpLev3id)
      #print(type(tmpLev3id))
      x = list(tmpLev3.CCID)
      print(tmpLev3)
      tmpLev3af = tmpLev3.sort_values("ccTerm")   
      print("before ↑ tmpLev3af = tmpLev3.sort_values(\"ccTerm\") after↓")
      print(tmpLev3af)



      tmpLev3af.CCID = x

      #print(tmp)

      if not tmpLev3idTmp: # If there is no more than Level3 CC terms
        #print("the list is empty Lv.3 Lv.3 Lv.3")

        #print("After arranging Level2 CC terms")
        #print(tmpLev2Daf)
        trueIdLev3 = list(tmpLev2Daf[tmpLev2Daf.ccTerm==rowL[1]].CCID)[0][0:5]
        print("tmpLev2Daf")
        print(tmpLev2Daf)
        print("rowL[1]")
        print(rowL[1])  # 例) CC0120000        OL   → "CC012"0000 (Trim off up to Lv.2 CC terms)


        #for indexL, rowL in tmpLev2Daf.iterrows():



        print("trueIdLev3")
        print(trueIdLev3)
        print("tmpLev3af")
        print(tmpLev3af)


        for index3, row3 in tmpLev3af.iterrows():
          # print("tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3")
          # print(tmpLev3)
          # print("---")
          # print("tmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3af")
          # print(tmpLev3af)

        
          tmpR3 = list(row3[0]) # n the case of OL, '0120' from 'CC0120000' will be written under Level 3 or below.
          tmpR3[2] = list(trueIdLev3)[2] # trueIdLev3は"CC013"
          tmpR3[3] = list(trueIdLev3)[3] # trueIdLev3は"CC013"
          tmpR3[4] = list(trueIdLev3)[4] # trueIdLev3は"CC013"
          tmpR = "".join(tmpR3)

          # CC01f1000   #女子学生
          # CC01f1100   #女子大生

          #if list(row3[1])[0] + list(row3[1])[1] + list(row3[1])[2] + list(row3[1])[3] + list(row3[1])[4] + list(row3[1])[5] + list(row[1])[6]
          if list(row3[0])[6] == "0":
            if list(row3[0])[7] == "0":
              if list(row3[0])[8] == "0":
                outF.write(tmpR + "\t" + row3[1] + "\n")
                #outF.write(row3[0] + "\t" + row3[1] + "\n")
                print(tmpR + "  " + row3[1]  + " " + "Level3")


      else: # If Level 3 and beyond continue (e.g., if it is a Level 3 school <CC0211000>, it means Level 3 and beyond continue)
        # print("tmpLev2tmpLev2tmpLev2tmpLev2tmpLev2tmpLev2tmpLev2tmpLev2")
        # print(tmpLev2D)
        # print("tmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3af")
        # print(tmpLev2Daf)
        # print("tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3tmpLev3")
        # print(tmpLev3)
        # print("---")
        # print("tmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3aftmpLev3af")
        # print(tmpLev3af)


        #print("true ID true ID true ID true ID true ID true ID")
        trueIdLev3 = list(tmpLev2Daf[tmpLev2Daf.ccTerm==rowL[1]].CCID)[0][0:5]  # 例) Obtain the CC term up to Level 2 in OL

        # CC0211000 → CC021 人工物→施設

        # CC013
        #if rowL[1] == "アイドル":
        #  break
        #true ID true ID true ID true ID true ID true ID
        #CC0

        #true ID true ID true ID true ID true ID true ID
        #['CC0130000']

        for index3, row3 in tmpLev3af.iterrows():
          tmpR3 = list(row3[0])
          tmpR3[2] = list(trueIdLev3)[2] # trueIdLev3 is "CC013"
          tmpR3[3] = list(trueIdLev3)[3] # trueIdLev3 is "CC013"
          tmpR3[4] = list(trueIdLev3)[4] # trueIdLev3 is "CC013"
          tmpR = "".join(tmpR3)
          #print("tmpR tmpR tmpR")
          #print(tmpR)

           # CC0211000 → CC021 人工物→施設

          if list(row3[0])[6] == "0":
            if list(row3[0])[7] == "0":
              if list(row3[0])[8] == "0":
                outF.write(tmpR + "\t" + row3[1] + "\n")
                #outF.write(row3[0] + "\t" + row3[1] + "\n")
                print(tmpR + "  " + row3[1]  + " " + "Level3")


          #outF.write(tmpR + "\t" + row3[1] + "\n")
          #print(tmpR + "  " + row3[1]  + " " + "Level3")

          #outF.write(row3[0] + "\t" + row3[1] + "\n")

        #print("The list is not empty Lv.3 Lv.3 Lv.3")
        # 例) → 'CC01i1000', 'CC01i2000', 'CC01i3000', 'CC01i4000', 'CC01i5000', 'CC01i6000', 'CC01i7000', 'CC01i8000'] about idols
        #         CC01i0000 is the parent 
        # print(tmpLev3id)
        #print(curOntoD[curOntoD.CCID.isin(tmpLev3id)])  # Display the lower term of idol


        tmpLev4 = curOntoD[curOntoD.CCID.isin(tmpLev3id)] #CCID, ccTerm  # Level3 or more CC term is "tmpLev3id"





        print("for indexM, rowM in tmpLev4.iterrows():")
        print(tmpLev4)


        tmpCcid = list(tmpLev4.CCID)
        svIDs = []
        resIDs = []
        for tid in tmpCcid:
          if list(tid)[5] not in svIDs:
            svIDs.append(list(tid)[5])
            resIDs.append(tid)

        tmpLev4Lim = tmpLev4[tmpLev4.CCID.isin(resIDs)]  # This will eliminate duplicate values for Level 3.
        print("tmpLev4Lim")
        print(tmpLev4Lim)
        print("svIDs")
        print(svIDs)


        for indexM, rowM in tmpLev4Lim.iterrows(): # Processing when Level 4 is included (Why a for loop??? The reason is to handle cases like CC0871XXX and CC0872XXX)
          # CC0871000 →　CC0871 (the first loop)
          # CC0871100 →  CC0871 (the second loop)
          # CC0871110 →  CC0871 (the thirt loop)
          tmpTarId4 = list(rowM[0])[0:6]  # 'CC01i1000 → CC01i1

          #print("tmpTarId4 tmpTarId4 tmpTarId4")
          #print(tmpTarId4)


          tmpLev4id = list(curOntoD[curOntoD.CCID.str.contains("".join(tmpTarId4))].CCID) #CC0871000, CC0871100 (女性の同性愛), CC0871110（百合）
          tmpLev4id.remove(rowM[0])


          tmpLev4idTmp = []
          for tL4 in tmpLev4id:           # Lv.              123456
            if list(tL4)[7] != "0":       # CC01i1000 →　CC01i1000   The position [7] corresponds to Level 5. If it is not 0, it is determined that Level 4 and beyond exist
              tmpLev4idTmp.append(tL4)

          #tmpLev4id = tmpLev4idTmp

          nowTmpDall = pd.DataFrame({
              'CCID' : [],
              'ccTerm' : []
          })

          #nowTmpD = []
          for index, tL4 in tmpLev4.iterrows():
            # If Level 5 is zero (because only Level 4 terms need to be sorted).  CC01f1100 女子大生
            if list(tL4[0])[6] != "0" and list(tL4[0])[7] == "0" and "".join(list(rowM[0])[0:6]) == "".join(list(tL4[0])[0:6]): 
               # CC0211000

            #if list(tL4[0])[7] == "0": # If Level 5 is zero (to sort only Level 4 terms)."  CC01f1100 女子大生


              #nowTmpD.append(tL4)
              nowTmpD = pd.DataFrame(
                  data = {
                      'CCID' : [tL4[0]],
                      'ccTerm' : [tL4[1]]
                  }
              )
              nowTmpDall = pd.concat([nowTmpDall, nowTmpD])
              #nowTmpD.append(tL4)

          #tmpLev4 = nowTmpDall # Avoid this because it is a destructive process!

          #tmpLev4 = tmpLev4[tmpLev4.CCID.isin(tmpLev4id)]  # May need this?

#                   CCID  ccTerm
# 0  CC0870000       愛
# 0  CC0871000     同性愛
# 0  CC0871100  女性の同性愛 (Lv.4)
# 0  CC0871110      百合


          x = list(nowTmpDall.CCID)
          tmpLev4af = nowTmpDall.sort_values("ccTerm")
          tmpLev4af.CCID = x

          if not tmpLev4idTmp:  # This will contain the CC term for Level 5 and beyond.
            #print("The list is empty Lv.4 Lv.4 Lv.4")

            #trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0][0:5]

            print("tmpLev3af")
            print(tmpLev3af)
            print("rowM[1]")
            print(rowM[1])
            print("tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID")
            print(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)
            print("list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)")
            print(list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID))


            #print("list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0]")
            #print(list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0])


            print("tmpLev3")
            print(tmpLev3)
            print("tmpLev3af")
            print(tmpLev3af)
            print(rowM[1])  # 女子大生  rowM[0] becomes CC01f1100

            #trueIdLev4 = list(list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0])[0:6]  # For Level 3, if it's 0:5, should it be increased one by one?
            #trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0][0:6]  # For Level 3, if it's 0:5, should it be incremented one by one?
            #list(tmpLev3af[tmpLev3af.CCID == list(rowM[1])[0:6]+"000"].CCID)[0] #CC01f2
            #list(tmpLev3af[tmpLev3.CCID == list(rowM[1])[0:6]+"000"].ccTerm)[0] #CC01f2

            # This process means: ① Refer to the original ID of the upper term of the current term. ② Refer to the new ID of the upper term from step ①
            #print()
            print("\"\".join(list(rowM[1])[0:6])+\"000\"")
            print("".join(list(rowM[0])[0:6])+"000")  # CC01f1000
            #print()

            print()

            trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm == list(tmpLev3[tmpLev3.CCID == "".join(list(rowM[0])[0:6])+"000"].ccTerm)[0]].CCID)[0][0:6]

            #trueIdLev3 = list(tmpLev2Daf[tmpLev2Daf.ccTerm==rowL[1]].CCID)[0][0:5]

# tmpLev3
#         CCID ccTerm
# 0  CC01f1000   女子学生 jyoshigakusei
# 0  CC01f2000   男子学生 (架空) danshi gakusei
# tmpLev3af
#         CCID ccTerm
# 0  CC01f1000   男子学生
# 0  CC01f2000   女子学生 (架空)


# tmpLev3af.ccTerm




            # CC01f0000 学生
            # CC01f1000 女子学生
            # CC01f2000 男子学生 (架空)
            # CC01f1100 女子大生
            # CC01f2100 男子大生 (架空)
            # ↑
            # in this case, CC01f1100

            # CC01f1000
            # CC01f2000
            # ↓
            # CC01f1100




            print("tmpLev4 tmpLev4 tmpLev4")
            print(tmpLev4)
            #    CCID               ccTerm
            # 0  CC0211000           学校         o
            # 0  CC0211100         美容学園       o
            # 0  CC0212000          ギルド        x
            # 0  CC0211200    メロディースクール  o
            # 0  CC0213000           神殿         x
            # 0  CC0213100         海底神殿       x
            # 0  CC0214000           銭湯         x
            # 0  CC0215000           パブ         x
            # 0  CC0216000          収容所        x
            # 0  CC0217000           お城         x
            # 0  CC0217100         氷のお城       x
            # 0  CC0218000         ラウンジ       x
            # 0  CC0219000         ダイナー       x
            # 0  CC0219100    アメリカンダイナー  x

            print("tmpLev4af tmpLev4af tmpLev4af")
            print(tmpLev4af)
            print("trueIdLev4 trueIdLev4 trueIdLev4")
            print(trueIdLev4)
            for index4, row4 in tmpLev4af.iterrows():
              tmpR4 = list(row4[0])
              tmpR4[2] = list(trueIdLev3)[2] # trueIdLev4 is "CC0131"
              tmpR4[3] = list(trueIdLev3)[3] # trueIdLev4 is "CC0131"
              tmpR4[4] = list(trueIdLev3)[4] # trueIdLev4 is "CC0131"
              tmpR4[5] = list(trueIdLev4)[5] # trueIdLev4 is "CC0131"    # 学校だったら，CC021"h"

              # tmpR4[2] = list(trueIdLev4)[2] # trueIdLev4は"CC0131"
              # tmpR4[3] = list(trueIdLev4)[3] # trueIdLev4は"CC0131"
              # tmpR4[4] = list(trueIdLev4)[4] # trueIdLev4は"CC0131"
              # tmpR4[5] = list(trueIdLev4)[5] # trueIdLev4は"CC0131"
              tmpR = "".join(tmpR4)
                                          #   123456 (Lv)
              if list(row4[0])[6] != "0": #CC01f1100 → CC01f1"1"00  # If the position of Level 4 is not zero, it should not be zero because it is Level 4.
                if list(row4[0])[7] == "0": #CC01f1100 → CC01f11"0"0 # If the position of Level 5 is zero, it should not be zero because it is Level 4, and Level 5 cannot be zero.
                  if list(row4[0])[8] == "0": #CC01f1100 → CC01f110"0" # If the position of Level 6 is zero.
                    if list(rowM[0])[5] == list(row4[0])[5]:
                      outF.write(tmpR + "\t" + row4[1] + "\n")
                      print(tmpR + "  " + row4[1]  + " " + "Level4 通常の場合")



            #pass
          else:
            print("tmpLev4 tmpLev4 tmpLev4")
            print(tmpLev4)
            print("tmpLev4id tmpLev4id tmpLev4id")
            print(tmpLev4id)
            print("tmpLev4af tmpLev4af tmpLev4af")
            print(tmpLev4af)
            print("trueIdLev4 trueIdLev4 trueIdLev4")
            print(trueIdLev4)
            #trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm==rowM[1]].CCID)[0][0:6]
            trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm == list(tmpLev3[tmpLev3.CCID == "".join(list(rowM[0])[0:6])+"000"].ccTerm)[0]].CCID)[0][0:6]


            #print("this list is not empty Lv.4 Lv.4 Lv.4")
            #print(tmpLev4id)

            tmpLev5 = curOntoD[curOntoD.CCID.isin(tmpLev4id)]
            print(tmpLev5)

            for index4, row4 in tmpLev4af.iterrows():
              tmpR4 = list(row4[0])
              tmpR4[2] = list(trueIdLev3)[2] # trueIdLev4 is "CC0131"
              tmpR4[3] = list(trueIdLev3)[3] # trueIdLev4 is "CC0131"
              tmpR4[4] = list(trueIdLev3)[4] # trueIdLev4 is "CC0131"
              tmpR4[5] = list(trueIdLev4)[5] # trueIdLev4 is "CC0131"

              #tmpR4[2] = list(trueIdLev4)[2] # trueIdLev4は"CC0131"
              #tmpR4[3] = list(trueIdLev4)[3] # trueIdLev4は"CC0131"
              #tmpR4[4] = list(trueIdLev4)[4] # trueIdLev4は"CC0131"
              #tmpR4[5] = list(trueIdLev4)[5] # trueIdLev4は"CC0131"

              tmpR = "".join(tmpR4)
              #print("tmpR tmpR tmpR")
              #print(tmpR)                                         456 (Lv.)
              if list(row4[0])[6] != "0": #CC01f1100         CC0871100  女性の同性愛
                if list(row4[0])[7] == "0": #CC01f1100
                  if list(row4[0])[8] == "0": #CC01f1100
                    if list(rowM[0])[5] == list(row4[0])[5]:
                      outF.write(tmpR + "\t" + row4[1] + "\n")
                      print(tmpR + "  " + row4[1]  + " " + "Level4 elseの場合")



            #tmpLev5 = curOntoD[curOntoD.CCID.isin(tmpLev4id)] #CCID, ccTerm

            #print("tmpLev5 tmpLev5 tmpLev5")
            #print(tmpLev5)

            print("for indexO, rowO in tmpLev5.iterrows():")
            print(tmpLev5)

            # for index, tL5 in tmpLev5.iterrows(): # How about placing it before the for loop? (start)
            #   if list(tL5[0])[7] == "1" and list(tL5[0])[8] == "0":
            #       nowTmpD = pd.DataFrame(
            #           data = {
            #               'CCID' : [tL5[0]],
            #               'ccTerm' : [tL5[1]]
            #           }
            #       )
            #       nowTmpDall = pd.concat([nowTmpDall, nowTmpD])
            #   tmpLev5 = nowTmpDall                # How about placing it before the for loop? (end)

            for indexO, rowO in tmpLev5.iterrows(): # It seems that this is bringing over the ones from tmpLev5 and beyond (Lv.5, Lv.6, Lv.7, ...).
              print("rowO rowO rowO")
              print(rowO)
              tmpTarId5 = list(rowO[0])[0:7]  # 'CC01i1000 → CC01i10    #C0871100（女性の同性愛）→ C087110
              print("tmpTarId5 tmpTarId5 tmpTarId5")
              print(tmpTarId5)
              tmpLev5id = list(curOntoD[curOntoD.CCID.str.contains("".join(tmpTarId5))].CCID)
              tmpLev5id.remove(rowO[0])

              print("tmpLev5Id tmpLev5id tmpLev5id")
              print(tmpLev5id)


              tmpLev5idTmp = []
              for tL5 in tmpLev5id:
                if list(tL5)[8] != "0":   #CC01f110"0"   C0871100
                  tmpLev5idTmp.append(tL5)

              #tmpLev5id = tmpLev5idTmp  #This is harmful, a destructive process

              # print("if not tmpLev5id:")
              # print(tmpLev5id)
              if not tmpLev5id:
                continue



              nowTmpDall = pd.DataFrame({ # Since it is placed before the for loop, it will be omitted here.
                  'CCID' : [],
                  'ccTerm' : []
              })
              #for indexO, rowO in tmpLev5.iterrows():
              #        CCID    ccTerm
              #0  CC1011100    パティスリー
              #0  CC1011200    キャンディー
              #0  CC1011210  キャンディーの国
              #0  CC1011300       あめ玉
              #0  CC1011400     お菓子の国
              for index, tL5 in tmpLev5.iterrows():
                #if list(tL5[0])[8] == "0": # If Level 5 is zero (because only Level 4 terms need to be sorted).  CC01f110"0" 女子大生
                #if list(tL5[0])[8] == "0" and list(tL5[0])[7] == "1":

                #if list(tL5[0])[7] == "1" and list(tL5[0])[8] == "0": # I understand the second part. Exclusion of Level 6.

                print("if tL5[0] == tmpLev5id[0]:")
                print(tL5[0])
                print(tmpLev5id[0])
                for tL5xx in tmpLev5id:
                  if tL5[0] == tL5xx:
                #if tL5[0] == tmpLev5id[0]:  #Need to consider there are multiple "tmpLev5id"

                # Use this conditional branch to insert tmpLev5id."
                # When キャンディー，['CC1011210'] (キャンディーの国)

                    nowTmpD = pd.DataFrame(
                      data = {
                          'CCID' : [tL5[0]],
                          'ccTerm' : [tL5[1]]
                      }
                    )
                  #nowTmpD.append(tL5)
                    nowTmpDall = pd.concat([nowTmpDall, nowTmpD])
              # 同性愛(CC0871000)(Lv.3) →女性の同性愛(CC0871100)(Lv.4) → 百合(CC0871110)(Lv.5)

              #tmpLev5 = nowTmpDall # Stop this because it is a destructive process!!!
                print("tmpLev3 tmpLev3 tmpLev3")
                print(tmpLev3)
                print("tmpLev4 tmpLev4 tmpLev4")
                print(tmpLev4)
                print("tmpLev5 tmpLev5 tmpLev5")
              #print(tmpLev5)
                print(nowTmpDall)

              #tmpLev5 = tmpLev5[tmpLev5.CCID.isin(tmpLev5id)]  # May need?

              #tmpTarId5 = list(rowO[0])[0:7]  # 'CC01i1000 → CC01i10

              # tmpLev4 =
              #x = list(tmpLev5.CCID)
              x = list(nowTmpDall.CCID)
              #tmpLev5af = tmpLev5.sort_values("ccTerm")  # Stop this because it is a destructive process!!!
              tmpLev5af = nowTmpDall.sort_values("ccTerm")
              tmpLev5af.CCID = x

              if not tmpLev5idTmp:  # If no CC term exists for Level 5 and above
                #print("This list is empty Lv.5 Lv.5 Lv.5")

                #trueIdLev5 = list(tmpLev4af[tmpLev4af.ccTerm==rowM[1]].CCID)[0][0:7]
                print("list(rowO[0])")
                print(list(rowO[0]))                        #
                print("list(rowO[0])[0:7]")         #                                    1234
                print(list(rowO[0])[0:7])           # CC0871110 (百合) →　CC08711 → CC0871100 (女性の同性愛)
                print("\"\".join(list(rowO[0]))")
                print("".join(list(rowO[0])))
                print("".join(list(rowO[0])[0:7])+"00")
                #print("list(tmpLev4[tmpLev4.CCID == \"\".join(list(rowO[0])")
                #print(list(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0][0:7]))

                #print(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0])))

                print("tmpLev4 tmpLev4 tmpLev4")
                print(tmpLev4)  # CC0871100 女性の同性愛
                print(".join(list(rowO[0])[0:7])+00")
                print("".join(list(rowO[0])[0:7])+"00") #CC0871000
                print("list(tmpLev4[tmpLev4.CCID == \"\".join(list(rowO[0])[0:7])+\"00\"])")
                print(list(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0])[0:7])+"00"]))  # ['CCID', 'ccTerm']  There was no match!!!


                print("list(tmpLev4[tmpLev4.CCID == \"\".join(list(rowO[0])[0:7])+\"00\"].ccTerm)[0]")
                print(list(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0])[0:7])+"00"].ccTerm)[0])
                print("list(tmpLev4af[tmpLev4af.ccTerm == list(tmpLev4[tmpLev4.CCID == \"\".join(list(rowO[0])[0:7])+\"00\"].ccTerm)[0]].CCID)")
                print(list(tmpLev4af[tmpLev4af.ccTerm == list(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0])[0:7])+"00"].ccTerm)[0]].CCID))

                trueIdLev5 = list(tmpLev4af[tmpLev4af.ccTerm == list(tmpLev4[tmpLev4.CCID == "".join(list(rowO[0])[0:7])+"00"].ccTerm)[0]].CCID)[0][0:7]





                #trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm == list(tmpLev3[tmpLev3.CCID == "".join(list(rowM[0])[0:6])+"000"].ccTerm)[0]].CCID)[0][0:6]


                # CC0871000

                #trueIdLev4 = list(tmpLev3af[tmpLev3af.ccTerm == list(tmpLev3[tmpLev3.CCID == "".join(list(rowM[0])[0:6])+"000"].ccTerm)[0]].CCID)[0][0:6]


                for index5, row5 in tmpLev5af.iterrows():
                  tmpR5 = list(row5[0])
                  tmpR5[2] = list(trueIdLev3)[2] # trueIdLev5 is "CC01312"
                  tmpR5[3] = list(trueIdLev3)[3] # trueIdLev5 is "CC01312"
                  tmpR5[4] = list(trueIdLev3)[4] # trueIdLev5 is "CC01312"
                  tmpR5[5] = list(trueIdLev4)[5] # trueIdLev5 is "CC01312"
                  tmpR5[6] = list(trueIdLev5)[6] # trueIdLev5 is "CC01312"

                  #tmpR5[2] = list(trueIdLev5)[2] # trueIdLev5 is "CC01312"
                  #tmpR5[3] = list(trueIdLev5)[3] # trueIdLev5 is "CC01312"
                  #tmpR5[4] = list(trueIdLev5)[4] # trueIdLev5 is "CC01312"
                  #tmpR5[5] = list(trueIdLev5)[5] # trueIdLev5 is "CC01312"
                  #tmpR5[6] = list(trueIdLev5)[6] # trueIdLev5 is "CC01312"


                  tmpR = "".join(tmpR5)

                  print("before writing before writing before writing")
                  print("tmpLev4Lim")
                  print(tmpLev4Lim) # This forms rowM. The following loop is running under rowM. However, since this is before sorting, it needs to be aligned with the post-sort order
                  print("tmpLev4af")
                  print(tmpLev4af)  # This forms row4．


                  if list(row5[0])[7] != "0": # Level5 is not zero，
                    if list(row5[0])[8] == "0":
                      if list(rowO[0])[5] == list(row5[0])[5]:



                        #if list(row5[0][6] == list(rowO?[0][6])):  # Write it down if it is a concept under Level 4 (キャンディー), such as キャンディー王国.
                        #tmpLim4Lim's 'rowM is before sorting．After sorting is tmpLev4af's row4．

                        outF.write(tmpR + "\t" + row5[1] + "\n")
                        print(tmpR + "  " + row5[1]  + " " + "Level5")

             
              else:
                print("Exception！！！！！！！！！！！！！！！！！！！！！！！！")




if __name__ == "__main__":
    main()

