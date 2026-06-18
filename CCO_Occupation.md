```mermaid
graph TD

%% =====================
%% Root
%% =====================
A[CC0100000 Occupation / 職業]

%% =====================
%% Level 1 categories
%% =====================
A --> B[CC0110000 Music and Performance]
A --> C[CC0120000 Model and Talent]
A --> D[CC0130000 Food and Service]
A --> E[CC0140000 Education and Student]
A --> F[CC0150000 Medical and Nursing]
A --> G[CC0160000 Military / Police / Combat]
A --> H[CC0170000 Special and Fictional]
A --> I[CC0180000 Secretary and Administration]

%% =====================
%% Music and Performance
%% =====================
B --> B1[DJ]
B --> B2[Idol]
B --> B3[Live Streamer]
B --> B4[Voice Actor]

B2 --> B21[Idol Otaku]
B2 --> B22[Idol School]
B2 --> B23[Idol Development]
B2 --> B24[Gravure Idol]
B2 --> B25[Virtual Idol]
B2 --> B26[Orthodox Idol]
B2 --> B27[K-Pop Idol]
B2 --> B28[Drinkable Idol]

%% =====================
%% Model and Talent
%% =====================
C --> C1[Talent]
C --> C2[Model]
C --> C3[Photo Shoot Model]
C --> C4[Influencer]

%% =====================
%% Food and Service
%% =====================
D --> D1[Waitress]
D --> D2[American-Style Waitress]
D --> D3[Maid]
D --> D4[Store Manager]
D --> D5[One-Day Store Manager]
D --> D6[Other Service]

%% Maid subtypes
D3 --> D31[Kawaii Maid]
D3 --> D32[Animal-Eared Maid]
D3 --> D33[Tracksuit Maid]
D3 --> D34[Animal Maid]
D3 --> D35[Gothic Maid]
D3 --> D36[Chinese-Style Maid]
D3 --> D37[Bunny Maid]
D3 --> D38[Maid Outfit]
D3 --> D39[Bloodsucker Maid]
D3 --> D310[Japanese-Style Maid]
D3 --> D311[Assassin Maid]
D3 --> D312[Cat Robot Maid]
D3 --> D313[Cat-Eared Maid]
D3 --> D314[Ryukyuan Maid]
D3 --> D315[Magical Maid]
D3 --> D316[Magical Maid Institute]

%% =====================
%% Education / Student
%% =====================
E --> E1[Student]
E --> E2[Schoolgirl]
E --> E3[Female College Student]
E --> E4[Cheerleader]

%% =====================
%% Medical
%% =====================
F --> F1[Nurse]
F1 --> F2[Angel Nurse]

%% =====================
%% Military / Combat
%% =====================
G --> G1[Military]
G --> G2[Military Force]
G --> G3[Police Officer]
G --> G4[Anipoli]
G --> G5[Warrior]
G --> G6[Legendary Warrior]
G --> G7[Magical Warrior]
G --> G8[Assassin]
G --> G9[Assassin Maid (Assassin)]
