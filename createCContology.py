import pandas as pd
import numpy as np
import collections
import itertools
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns

def main(): # Based on the upperMap file, annotate the CC term into each corresponding ConCaffe.（for GitHub)

  cafeConpD = pd.read_csv("/YourPath/cLisTopX_manuV4.txt", sep="\t")

  topTerms = pd.read_csv("/YourPath/topTermsV2.txt", sep="\t")

  vList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

  outF = open("/YourPath/conceptCafeOntology.txt", "w")
  outF.write("CCID" + "\t" + "ccTerm" + "\n")

  for indexI, rowI in topTerms.iterrows():
    tmpIds = []
    tmpNames = []
    for indexJ, rowJ in cafeConpD.iterrows():
      if rowI[0] in rowJ[2]:
        if "OROR" in rowJ[2]: ########################## if "OROR" contains in the sentence ##############################
          curDor = rowJ[2].split("OROR") # Split with "OROR"
          for cdo in curDor:
            if rowI[0] in cdo: # If the specified Top CC term is included
              if "divdiV" in cdo: # ################## When "OROR" → "divdiv" → "upper" ##################
                curDdiv = cdo.split("divdiV")
                curDdiv = list(filter(None, curDdiv))
                for cdo3 in curDdiv:
                  if rowI[0] in cdo3: # If the specified Top CC term is included
                    curDdiv_ = cdo3.split("_")
                    curDdiv_ = list(filter(None, curDdiv_))
                    tmpUpSp = curDdiv_[0].split("upper")
                    tmpUpSp = list(filter(None, tmpUpSp))
                    vLcnt = 0
                    
                    tmpUpSp = list(reversed(tmpUpSp))
                    tmpUpSp.append(rowJ[0]) # This is the lowest CC term in actual
                    tmpUpSp.pop(0)  # Delete the Top CC term
                    for tsp in tmpUpSp:
                      tmpIds.append(vLcnt)
                      tmpNames.append(tsp)
                      vLcnt = vLcnt + 1
                    tmpIds.append("endendend")
                    tmpNames.append("endendend")
              else:  # ############################## if "OROR" → "upper" ################################
                tmpUpSp = cdo.split("upper")
                tmpUpSp = list(filter(None, tmpUpSp))
                vLcnt = 0

                tmpUpSp = list(reversed(tmpUpSp))
                tmpUpSp.append(rowJ[0]) # This is the lowest CC term in actual
                tmpUpSp.pop(0)  # Delete the Top CC term

                for tsp in tmpUpSp:
                  tmpIds.append(vLcnt)
                  tmpNames.append(tsp)
                  vLcnt = vLcnt + 1
                tmpIds.append("endendend")
                tmpNames.append("endendend")
        else: ########################## If there is no "OROR" ##############################
          if "divdiV" in rowJ[2]: # ################## if "divdiv" → "upper" ##################
                curDdiv =  rowJ[2].split("divdiV")
                curDdiv = list(filter(None, curDdiv))
                #curDdiv = list(filter(lambda x: x != "no", curDdiv))
                for cdo3 in curDdiv:
                  if rowI[0] in cdo3: # If the specified Top CC term is included
                    curDdiv_ = cdo3.split("_")
                    curDdiv_ = list(filter(None, curDdiv_))
                    #print(curDdiv_)
                    tmpUpSp = curDdiv_[0].split("upper")
                    tmpUpSp = list(filter(None, tmpUpSp))

                    vLcnt = 0
                    tmpUpSp = list(reversed(tmpUpSp))
                    tmpUpSp.append(rowJ[0]) # This is the lowest CC term in actual
                    tmpUpSp.pop(0)  # Delete the Top CC term
                    for tsp in tmpUpSp:
                      tmpIds.append(vLcnt)
                      tmpNames.append(tsp)
                      vLcnt = vLcnt + 1
                    tmpIds.append("endendend")
                    tmpNames.append("endendend")
          else: ######################### If "upper" ##############################
            tmpUpSp = rowJ[2].split("upper") # メイド，upper職業
            tmpUpSp = list(filter(None, tmpUpSp))
            #print(tmpUpSp)
            vLcnt = 0


            #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #print(tmpUpSp)
            tmpUpSp = list(reversed(tmpUpSp))
            #print(tmpUpSp)
            #print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            tmpUpSp.append(rowJ[0]) # This is the lowest CC term in actual

            tmpUpSp.pop(0)  #  Delete the Top CC term

            for tsp in tmpUpSp: # ["職業"]
              tmpIds.append(vLcnt)
              tmpNames.append(tsp)
              vLcnt = vLcnt + 1
            tmpIds.append("endendend")
            tmpNames.append("endendend")

    #print(tmpIds)
    #print(tmpNames)
    #print(len(tmpIds))
    #print(len(tmpNames))

    tmpIdNd = pd.DataFrame(
      data={
        'ccid' : tmpIds,
        'ccName' : tmpNames
      }
    )
    #print(tmpIdNd) # 71 rows
    #print(tmpIdNd.drop_duplicates()) #64 rows
    #tmpIdNd = tmpIdNd.drop_duplicates()
    #pd.set_option('display.max_rows', None)
    #print(tmpIdNd)

    ccTmpNs = []
    for indexJ, rowJ in tmpIdNd.iterrows():
      if rowJ[0] == 0:
        ccTmpNs.append(rowJ[1])
    #print(ccTmpNs)
    #print(list(set(ccTmpNs)))
    #ccTmpNs = sorted(list(set(ccTmpNs)))

    tmpIdNdv2 = pd.DataFrame(
        data = {
             'ccid' : [],
              'ccName' : [],
              'group' : []
        }
    )
    tmp1 = []
    tmp2 = []
    grpCnt = 0
    resDf = ""
    grpnameCnt = 1
    for indexJ, rowJ in tmpIdNd.iterrows():
      if rowJ[0] == "endendend":
        #print(['group' + str(indexJ)] * grpCnt)
        tmpDf = pd.DataFrame(
            data = {
                'ccid' : tmp1,
                'ccName' : tmp2,
                'group' : ['group' + str(grpnameCnt)] * grpCnt
            }
        )
        tmpIdNdv2 = pd.concat([tmpIdNdv2, tmpDf])
        tmp1 = []
        tmp2 = []
        grpCnt = 0
        grpnameCnt = grpnameCnt + 1
      else:
        tmpDf = ""
        tmp1.append(rowJ[0])
        tmp2.append(rowJ[1])
        grpCnt = grpCnt + 1

    #print(tmpIdNdv2)
    #print(ccTmpNs)

    topIndex = 0
    ccOntology = pd.DataFrame(
        data = {
            'ccid' : [],
            'ccName' : []
        }
    )


    #idIni = "CC010000" # The 4th level is Lv.2 (e.g., Maid<メイド>), and the 5th level is Lv.1 (e.g., Occupation<職業>).
    idIni = rowI[2]


    outF.write(rowI[2] + "\t" + rowI[0] + "\n")


    # CC011000→CC01"1"000 メイド
    # CC011100→CC011"1"00 猫耳メイド
    #ccidCnt = 1
    topPam = ["1","2","3","4","5","6","7","8","9",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #print(topIndex)
    #print(topPam)
    #print("topPam[topIndex]")
    #print(topPam[topIndex])
    #print("---")
    ccTmpNs = list(set(ccTmpNs))
    for cc in ccTmpNs:
      idDiv = list(idIni) #  Starting creation of the ID (ID decomposition).
      #print("idDiv")
      #print(idDiv)
      #print("topIndex")
      #print(topIndex)
      idDiv[4] = topPam[topIndex]
      #idDiv[4] = str(topIndex) # Update the id
      idDiv = ''.join(idDiv) # recombine the ids


      tmp1 = []
      tmp2 = []
      curD = tmpIdNdv2[tmpIdNdv2.ccName == cc] # Extract only the hierarchical relationships where the description is "Maid or something else."



      tmp1.append(idDiv)  # Add the CC term for "Maid" (メイド) (automatically created).
      tmp2.append(cc) #Add "Maid" (メイド)

      thisGrp = ""
      mLowCnt = 0 # Count for Lv.1
      mLowCntLv2 = 0 # Count for Lv.2
      mLowCntLv3 = 0 # Count for Lv.3

      #print("list(set(curD.group)")
      #print(list(set(curD.group)))

      #print("tmpIdNdv2 tmpIdNdv2 tmpIdNdv2")
      #print(tmpIdNdv2)
      #if cc == "サブカルチャー":
      tmpIdNdv2 = tmpIdNdv2[tmpIdNdv2.ccName != "なし"]
      #print("after after after after after after ")
      #print(tmpIdNdv2)
      #break

      for cdg in list(set(curD.group)):
        thisGrp = tmpIdNdv2[tmpIdNdv2.group==cdg] # Get the list of groups for "Maid" (e.g.)
        #print("thisGrp this Grp this Grp this Grp this Grp this Grp")
        #print(thisGrp)
        #break
        #if thisGrp.ccName[0] == cc:
        #  continue
          #print(thisGrp.ccName[0])
          #print(cc)
          #print("***")
        #if thisGrp.ccName[0] == cc:
        #  continue

        #idIni = list(idIni)

        #tmpLevD = list(set(curD.ccid))
        tmpLevD = list(set(thisGrp.ccid))
        #print("tmpLevD tmpLevD tmpLevD")
        #print(tmpLevD)

        #print("tmpLevD")
        #print(tmpLevD)
        tmpLevD = list(filter(lambda x: x != 0, tmpLevD))
        tmpLevD = sorted(tmpLevD)
        #print("tmpLevD tmpLevD tmpLevD")
        #print(tmpLevD)
        #curDdiv = list(filter(lambda x: x != "no", curDdiv))

        #悪	1	upper悪
        # print("or thisGrp.ccName[0] != cc:")
        # print(thisGrp)
        # print(thisGrp.ccName)
        # print(thisGrp.ccName[0])
        # print(cc)
        if tmpLevD:
        #and thisGrp.ccName[0] != cc:
          #if thisGrp.ccName[0] == cc:
          #  continue
        #if tmpLevD:
          #print("tmpLevD tmpLevD tmpLevD")
          #print(tmpLevD)
          contiCnt = []
          for ttt in tmpLevD: # when 女子大生upper女子学生upper学生，[0,1,2]
            #curDv2 = curD[curD.ccid == ttt] #If 猫耳メイド, 1
            curDv2 = thisGrp[thisGrp.ccid == ttt] #If 猫耳メイド, 1
            v2ccNs = sorted(curDv2.ccName) # The lower-level "Cat-ear Maid" should also be included under "Maid."

            #CC01b000 学生
            #CC01b100 女子学生
            #CC01b120 女子大生
            tmpCdv2 = ""
            for cdv2 in curDv2.ccName:
              tmpCdv2 = cdv2
            if tmpCdv2 in tmp2:
              contiCnt.append(1)
              continue
            else:
              contiCnt.append(0)

            mLowPam = ["1","2","3","4","5","6","7","8","9",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

            #forcedmLowPam = ["1","2","3","4","5","6","7","8","9",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

            alpAndNum = pd.DataFrame(
              data = {
                'num' : list(range(0,62)),
                'numAlf' : ["0", "1","2","3","4","5","6","7","8","9",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
              }
            )


            for nmLow in v2ccNs: #
              idDiv = list(idDiv)


              if list(thisGrp.ccName)[-1] == "動物園":
                print(thisGrp)
                print(idDiv)
              if ttt == 1:  # ccidのLevelが1までの場合（例：「お茶」→お茶会→秘密のお茶会）
                #print(mLowCnt)
                #print(mLowPam)

                if list(thisGrp.ccName)[-1] == "動物園":
                  print("tmp1 tmp1 tmp1")
                  print(tmp1[-1])
                  print(list(tmp1[-1])[5])
                  print(idDiv)
                  print(mLowCnt)
                  print(mLowPam[mLowCnt])

                if tmp1:
                  #print("list(tmp1[-1])[5] # 前のidの番号")
                  #print(list(tmp1[-1])[5]) # 前のidの番号(例：a)．
                  #print("alpAndNum[alpAndNum.numAlf==str(list(tmp1[-1][5]))]")

                  #print("alpAndNum[alpAndNum.numAlf ==" )
                  #print(alpAndNum[alpAndNum.numAlf == "0"])
                  #print("alpAndNum[alpAndNum.numAlf == str(list(tmp1[-1][5]))]")
                  #print("x = str(list(tmp1[-1][5]))")

                  #x = list(tmp1[-1][5]) # 前のcc IDの番号の一部を取得 # そうか，これはだめなのである．

                  t1D = []
                  for t1 in tmp1:
                    t1D.append(list(t1)[5])
                  t1D = sorted(t1D, reverse = True)[0]  # Get the maximum value of Level 1 so far, such as "a".

                  #alpAndNum[alpAndNum.numAlf == str(t1D)].num

                  t1DLas = alpAndNum.numAlf[list(alpAndNum[alpAndNum.numAlf == t1D].num)[0] + 1]  # the number os updated （string type）

                  #print(alpAndNum.numAlf[list(alpAndNum[alpAndNum.numAlf == "a"].num)[0] + 1])


                  # C
                  #CC0218000	ダイナー # before 3
                  #CC0218100	アメリカンダイナー # before 2
                  #CC0211300	魔法学校 # before 1




                  #print(x[0])

                  #print("result result result")

                  #xx = alpAndNum[alpAndNum.numAlf == str(x[0])]   # exchange into a number

                  #print(xx)
                  #print(alpAndNum.numAlf[xx.num[0]+1])  # become1

                  # ① Convert the previous ID to a number (e.g., if it's "a," it becomes 9).
                  # ② Increment the number from ① by 1, and then convert it back to a letter.
                  # ③ assign the value


                  #print("x")
                  #print(x)
                  #print("x[0]")
                  #print(x[0])
                  #print("str(list(tmp1[-1][5]))")
                  #print(str(list(tmp1[-1][5])))

                     # num   numAlf
                     #  0      0

                  #print(alpAndNum[alpAndNum.numAlf==str(list(tmp1[-1][5]))])    # 0

                  #print(alpAndNum.numAlf[0])
                  #print("xx.num[0]")
                  #print(xx)
                  #print(list(xx.num)[0])
                  #print(xx.num[0])

                  idDiv[4+int(ttt)] = t1DLas

                  #idDiv[4+int(ttt)] = alpAndNum.numAlf[list(xx.num)[0]+1] # exchange the string type by adding 1


                  #idDiv[4+int(ttt)] = mLowPam[alpAndNum[alpAndNum.numAlf==str(list(tmp1[-1][5]))].num]



                  #list indices must be integers or slices, not Series


                  #print("idDiv")
                  #print(idDiv)
                  #idDiv[4+int(ttt)] =

                  #print("mLowPam[int(list(tmp1[-1])[5])]")
                  #print(mLowPam[int(list(tmp1[-1])[5])])


                  #idDiv[4+int(ttt)] = mLowPam[int(list(tmp1[-1])[5])]

                  #idDiv[4+int(ttt)] = str(int(list(tmp1[-1])[5]) + 1)

                  #['C', 'C', '0', '1', 't', '9', '0', '0', '0']
                  #['C', 'C', '0', '1', 't', 'a', '0', '0', '0']

                  #idDiv[4+int(ttt)] = str(int(list(tmp1[-1])[5]) + 1)
                  idDiv[6] = "0"  # Initialize Level2
                  idDiv[7] = "0"  # Initialize Level3
                  idDiv[8] = "0"  # Initialize Level4
                else:
                  idDiv[4+int(ttt)] = mLowPam[mLowCnt]


              elif ttt == 2:  # If CC term Level is upt to 2（例：お茶→「お茶会」→秘密のお茶会）
                # if v2ccNs[0] == "魔法メイド学院":
                #   print("魔法メイド学院 魔法メイド学院 魔法メイド学院 魔法メイド学院 魔法メイド学院")
                #   print("thisGrp.ccName[0]")
                #   print(thisGrp.ccName[0])
                #   print("thisGrp.ccName[1]")
                #   print(thisGrp.ccName[1])
                #   print("tmp2")
                #   print(tmp2)

                # if v2ccNs[0] == "メロディースクール":
                #   print("v2ccNs v2ccNs v2ccNs")
                #   print(v2ccNs)
                #   print(v2ccNs[0])
                #   print(tmp2)
                #   print("thisGrp thisGrp thisGrp")
                #   print(thisGrp)
                #   print("tmpLevD tmpLevD tmpLevD")
                #   print(tmpLevD)
                  #['施設', '学校', '魔法学校', '軽音部', 'お城', '氷のお城', '動物園', 'アミューズメントパーク', '遊園地', '社交場', '夜の社交場', '収容所', 'スナック', '教会', '監獄', 'リゾート']

                #print()
                if thisGrp.ccName[1] in tmp2: # If CC term of Level 1 is previously appeared
                  if list(thisGrp.ccName)[-1] == "動物園":
                    print(thisGrp.ccName)
                    print(thisGrp.ccName[1])
                    print(tmp2)

                  #print("thisGrp thisGrp thisGrp")
                  #print(thisGrp)
                  #print("thisGrp.ccName")
                  #print(thisGrp.ccName)
                  #print("thisGrp.ccName[1]")
                  #print(thisGrp.ccName[1])
                  #print("tmp1 tmp1 tmp1")
                  #print(tmp1)
                  #print("tmp2 tmp2 tmp2")
                  #print(tmp2)

                  #missedID = list(tmp1[tmp1.index(int(thisGrp.ccid[1]))]) # "CC0214000" 学校
                  #missedID = list(tmp1[1]) # "CC0214000" 学校
                  missedID = tmp1[tmp2.index(thisGrp.ccName[1])]

                  #print("missedID missedID missedID")
                  #print(missedID)


                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedID)
                  # missedID = ''.join(missedID[0:6]) # "CC0214" a part of school (There might be existing concepts under this subcategory)
                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedID)
                  # #missedIDsss = missedID in tmp1 # Find the last numbering under the subcategory of "school." ( for example, there may be CC0214100, CC0214200, CC0214300)
                  missedIDsss = [s for s in tmp1 if "".join(missedID) in s]

                  if list(thisGrp.ccName)[-1] == "動物園":
                    print("missedID")
                    print(missedID)
                    print("missedIDsss")
                    print(missedIDsss)

                  #l = ['CC01r0000', 'CC01r1000']
                  #l_in = [s for s in l if 'CC01r1' in s]
                  #print(l_in)


                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedIDsss)
                  # #print(missedIDsss) # why "false" appears?
                  #print("missedID missedID missedID")
                  #print(missedID)
                  #print(tmp2)
                  #print(tmp1)
                  #print(missedID)
                  #print("missedIDsss before")
                  #print(missedIDsss)
                  #print(sorted(missedIDsss[-1]))
                  #print(list(sorted(missedIDsss[-1])))
                  #print(list(sorted(missedIDsss[-1]))[0:6])
                  #missedIDsss = list(sorted(missedIDsss)[-1])[0:6]  # CC0141000 → CC0141

                  #print("sorted("".join(list(missedIDsss)[0:6]) in tmp1)")
                  #print(list(missedIDsss[0])[0:6])
                  #print("".join(list(missedIDsss[0])[0:6]))
                  tmpParIDddd = "".join(list(missedIDsss[0])[0:6])  # CC0212000 → CC02120



                  #print("".join(list(missedIDsss[0])[0:6]) in tmp1) # for example， as 学校 CC0233000 → CC0233

                  tmpMissedIDsss = [s for s in tmp1 if tmpParIDddd in s]
                  missedIDsss = list(sorted(missedIDsss)[-1])  # CC0141000
                  #missedIDsss = sorted(tmpMissedIDsss)
                  #print("sorted missedIddddddddddddddddddd")
                  tmpMissedIDsss = sorted(tmpMissedIDsss)
                  tmpMissedIDsss.reverse()

                  if list(thisGrp.ccName)[-1] == "動物園":
                    print("tmpParIDddd")
                    print(tmpParIDddd)
                    print("tmpMissedIDsss")
                    print(tmpMissedIDsss)
                    print("missedIDsss")
                    print(missedIDsss)
                    print("tmpMissedIDsss")
                    print(tmpMissedIDsss)
                    print("tmpMissedIDsss")
                    print(tmpMissedIDsss)

                  #print("list(sorted(missedIDsss)[-1])")
                  #print("sorted(missedIDsss)")
                  #print(sorted(missedIDsss))
                  #print("sorted(missedIDsss)[-1]")
                  #print(sorted(missedIDsss)[-1])
                  #print("list(sorted(missedIDsss)[-1])")
                  #print(list(sorted(missedIDsss)[-1]))

                  # print("CC0233")
                  # tmpL = ['CC0233000', 'CC0233100', 'CC0233200']
                  # tmpLs = sorted(tmpL)
                  # tmpLs.reverse()
                  # print(tmpLs)



                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedIDsss)
                  # print("missedIDsss missedIDsss missedIDsss")
                  #print(missedIDsss)
                  missedIDsss = list(tmpMissedIDsss[0])

                  #No C128XXX, but filter as CC1281X00
                  missedIDsss[-1] = '0'
                  missedIDsss[-2] = '0'


                  #print("missedIDsss[6] = str(int(missedIDsss[6]) + 1)")
                  missedIDsss[6] = str(int(missedIDsss[6]) + 1) # Register it as the nth item under the subcategory of "school."
                  #print("missedIDsss after")
                  #print(missedIDsss)
                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedIDsss[6])
                  # #missedIDsss.append(0)
                  # missedIDsss.append(0)
                  # missedIDsss.append(0)
                  # if v2ccNs[0] == "メロディースクール":
                  #   print(missedIDsss)
                  idDiv = missedIDsss


                  #x = ["CC0214300", "CC0214100", "CC0214200"]
                  #print(sorted(x))
                  #print(sorted(x)[-1])
                  #x = list("CC0214000")
                  #print(''.join(x[0:6]))

                  #idDiv = list(tmp1[tmp1.index(v2ccNs[0])]) # Become CC term（e.g. → CC term description "school" above "Melody school"  (CC0214000 → CC0214100)
                  # と思うのだが，

                else:
                  idDiv[4+int(ttt)] = mLowPam[mLowCntLv2]



                # x = ["a", "b", "c"]
                # if "b" in x:
                #   print(x.index("b"))


              elif ttt == 3:  # When CC term Level is 3（e.g.：お茶→お茶会→「秘密のお茶会」）
                #idDiv[4+int(ttt)] = mLowPam[mLowCntLv3] 
                if thisGrp.ccName[2] in tmp2: # if CC term Level 2（例：お茶会）is previousely appeared
                  missedID = tmp1[tmp2.index(thisGrp.ccName[2])] # Get the Level 2 CC term of Level2（例：お茶会）
                  missedIDsss = [s for s in tmp1 if "".join(missedID) in s] # ???
                  tmpParIDddd = "".join(list(missedIDsss[0])[0:7]) # CC1282100 → CC128210  # Look for the maximum term of this level (e.g.: if CC1282122, becomes CC128212"3"")
                  tmpMissedIDsss = [s for s in tmp1 if tmpParIDddd in s]
                  missedIDsss = list(sorted(missedIDsss)[-1])
                  tmpMissedIDsss = sorted(tmpMissedIDsss)
                  tmpMissedIDsss.reverse()
                  missedIDsss = list(tmpMissedIDsss[0])
                  missedIDsss[7] = str(int(missedIDsss[7]) + 1) # Register it as the nth item under the subcategory of "xxx."
                  idDiv = missedIDsss
                else:
                  idDiv[4+int(ttt)] = mLowPam[mLowCntLv3] # If the Level 2 CC term ("Tea Party") is the first appearance, the value of Level 3 will be 0.

              idDiv = ''.join(idDiv)
              tmp1.append(idDiv)
              tmp2.append(tmpCdv2)
              # if ttt == 3:
              #   print(idDiv)
              #   print(tmpCdv2)

              # if cc == "店内サービス":
              #   print(idDiv)
              #   print(tmpCdv2)
              #   print("---")

          if len(tmpLevD) == 1 and sum(contiCnt) != len(tmpLevD): # If it ends at Level 1, increment the value.（例: アニマルメイドupperメイド）
          #if len(tmpLevD) == 1 and contiCnt == 0: # If it ends at Level 1, increment the value.（例: アニマルメイドupperメイド）
          #if len(tmpLevD) == 1: # If it ends at Level 1, increment the value.（例: アニマルメイドupperメイド）

            mLowCnt = mLowCnt + 1


          # elif len(tmpLevD) == 2:
          #   if list(thisGrp.ccName)[-1] == "お菓子の国":


            if sum(contiCnt) == 0: 
            #if contiCnt[1] == 1:
              mLowCnt = mLowCnt + 1
            elif contiCnt[0] == 0: 
              mLowCnt = mLowCnt + 1





              tmp1tmp = tmp1[tmp2.index(thisGrp.ccName[1])] #
              tmp1tmp = list(tmp1tmp) #CC023s"0"00 
              tmp1tmp[6] = "1"
              tmp1tmp = "".join(tmp1tmp)
              tmp1.append(tmp1tmp)
              tmp2.append(thisGrp.ccName[2])


              # x = ["a", "b", "c"]
              # if "b" in x:
              #   print(x.index("b"))


            idDiv = list(idDiv) # To generate the next ccID, initialize the position of Level 2.
            idDiv[4+2] = "0"
            idDiv = ''.join(idDiv)


          elif len(tmpLevD) == 3:  # 0,1,2,3 → 0(店内サービス[-1]→飲み物[0]→お茶[1]→お茶会[2]→秘密のお茶会[3])
            plusFlag = 0
            #print(tmp1tmp)
            #print(thisGrp.ccName[2])
            #print(thisGrp)
            #print("---")
            if sum(contiCnt) == 0:  # In the case of no duplicates at any level.
              mLowCnt = mLowCnt + 1 # Update the count valuable for Lv.1
              plusFlag = 1
            elif contiCnt[0] == 0: # If CC term with Level1 is new
              mLowCnt = mLowCnt + 1
              plusFlag = 1
              tmp1tmp = tmp1[tmp2.index(thisGrp.ccName[1])] 
              tmp1tmp = list(tmp1tmp) #CC023s"0"00 
              tmp1tmp[6] = "1"
              tmp1tmp = "".join(tmp1tmp)
              tmp1.append(tmp1tmp)
              tmp2.append(thisGrp.ccName[2])
            if contiCnt[1] == 0:  # If CC term with Level2 is new
              if plusFlag == 0:
                mLowCnt = mLowCnt + 1
              #mLowCntLv2 = mLowCntLv2 + 1 
              # tmp1tmp = tmp1[tmp2.index(thisGrp.ccName[2])] # Get CC term with Lv.2 level
              # tmp1tmp = list(tmp1tmp)                       # CC023s0"0"0
              # tmp1tmp[7] = "1"                              
              # tmp1tmp = "".join(tmp1tmp)
              # tmp1.append(tmp1tmp)
              # tmp2.append(thisGrp.ccName[3])
              # print(tmp1tmp)
              # print(thisGrp.ccName[3])
              # print("---")

            #print(idDiv)

            idDiv = list(idDiv) # To generate the next CC term, initialize the positions of Level 2 and Level 3.  (例：CC1281210<キャンディーの国> → CC1281000<お菓子>)
            idDiv[4+2] = "0"  # Initialize Level2
            idDiv[4+3] = "0"  # Initialize Level3
            idDiv = ''.join(idDiv)


        tmpDf = pd.DataFrame(
          data = {
            'ccid' : tmp1,
            'ccName' : tmp2
          }
        )
        #print("tmpDf tmpDf tmpDf")
        #print(tmpDf)
      ccOntology = pd.concat([ccOntology, tmpDf])
      #CCID ccTerm
      #ccOntology
      topIndex = topIndex + 1


    pd.set_option('display.max_rows', None)
    #if cc == "店内サービス":
    #print(ccOntology)
    #print("ccccccccccccccccccccccccc")
    #print(cc)


    for indexX, rowX in ccOntology.iterrows():
      outF.write(rowX[0] + "\t" + rowX[1] + "\n")


if __name__ == "__main__":
    main()


