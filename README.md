# ConCafe
This site collects data on concept cafes (ConCafes) in Tokyo, Japan, for the year 2024 from a website called Moesta+, and classifies the concepts of these cafes in a quantitative manner. The results are expected to be classified from the perspectives of comprehensiveness and trends. This classification provides answers to questions such as "What kind of concepts exist in ConCafes?" and "What are the trends in concepts of ConCafes?", offering insights for those who have recently become interested in ConCafes. It also provides hints for those looking to open a ConCafe in the future.

Below is an explanation of the files uploaded here.

・conceptCafeOntologySortedLas.txt<p>
&nbsp;&nbsp;This is a table of correspondences between a CC term and its description. <p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "ccTerm" column is the ID used to uniquely identify the concept of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "Description" column contains the description of the concept of the ConCafe written in Japanese.<p>
<p>
・cafeNameCCtermsRepSt.txt<p>
&nbsp;&nbsp;This is a table of correspondences between a ConCafe (Anonymized ID description) and its annotated CC terms. <p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "CCafeName" column is a ConCafe (Anonymized ID description). <p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "ccTerms" column is a CC term. <p><p>

・ConCafeAllData.txt<p>
&nbsp;&nbsp;This is a table of a ConCafe with its attributes. <p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "cafeId" column is an ID that uniquely represents an anonymized ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "openDate" column is the opening month and year of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "oneHourFee" column is the price of all-you-can-drink, calculated on an hourly basis.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "closedDate" column is the closing date of a ConCafe. ConCafes that continued until July 2024 are marked with "c".<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "Age" column is the age of a ConCafe. It is calculated by subtracting the opening date from the closing date. If the cafe has not closed, the year is considered to be November 2024.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "sYear" column is the opening year of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "sMonth" column is the opening month of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "eYear" column is the closed year of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "eMonth" column is the closed month of a ConCafe.<p>
&nbsp;&nbsp;&nbsp;&nbsp;- The "nofXfollower" column is the number of a ConCafe's X followers（As of November 2024).<p><p>



