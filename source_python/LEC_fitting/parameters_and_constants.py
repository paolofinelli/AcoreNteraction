import numpy as np
MeVfm = 197.3161329

lec_list_c = {}
lec_list_oneMEV_orig = {}
lec_list_one_four = {}
lec_list_one_three = {}
lec_list_one_onefive = {}

lec_list_one_onefive['137'] = {
    '0.10': [-2.241713349852539, -1.7100974855804583],
    '0.15': [-3.0711601037169327, -2.6943349906512393],
    '0.20': [-4.0403177472861325, -4.035469410666921],
    '0.25': [-5.1486159644240015, -5.74970611340178],
    '0.30': [-6.396653671611328, -7.930355617620481],
    '0.35': [-7.7840500433007795, -10.625338250678968],
    '0.40': [-9.310284894570248, -13.905072371852459],
    '0.45': [-10.976382994715028, -17.813427846033512],
    '0.50': [-12.781292360262205, -22.86622935468719],
    '0.55': [-14.72614191422407, -28.04364043938964],
    '0.60': [-16.809452231875916, -34.91384578401303],
    '0.65': [-19.032172290830918, -43.41002387926454],
    '0.70': [-21.393484854440914, -52.62746496306807],
    '0.75': [-23.895741635404175, -64.14944993454407],
    '0.80': [-26.535099029892574, -77.13694158176557],
    '0.85': [-29.315055618403697, -84.24808011823765],
    '0.90': [-32.23368625650024, -110.50799534991582],
    '0.95': [-35.29201267388672, -123.94835562168655],
    '1.00': [-38.487548474358775, -154.56723073029988],
    '1.05': [-41.82448197237221, -166.16505658232944],
    '1.10': [-45.29844044685785, -214.5831642828261],
    '1.15': [-48.91247325111309, -251.29047327160455],
    '1.20': [-52.66811542305018, -291.2827135488995],
    '1.25': [-56.5590095512287, -343.52535054944855],
    '1.30': [-60.59167601428699, -395.84213749935867],
    '1.35': [-64.76195112247063, -467.6740449089534],
    '1.40': [-69.07288801806678, -538.3011823143347],
    '1.45': [-73.5229991204783, -621.3881305861289],
    '1.50': [-78.10941443906269, -728.5320003854471],
    '1.55': [-82.8376801686698, -852.5956662700384],
    '1.60': [-87.70187974527865, -983.4523862000772],
    '1.65': [-92.71051776501592, -1138.2892828513463],
    '1.70': [-97.85495024904827, -1274.929485792135],
    '1.75': [-103.13585979326862, -1516.686024280938],
    '1.80': [-108.56079499288674, -1678.0174264871193],
    '1.85': [-114.12497186109528, -2043.2828841093954],
    '1.90': [-119.82399700307546, -2334.9054029199697],
    '1.95': [-125.66490273845393, -2745.3998060624745],
    '2.00': [-131.64811012515355, -3062.8315372777515],
    '2.05': [-137.77069472280215, -3649.2198641061304],
    '2.10': [-144.01858521350738, -2101.0727972865457],
    '2.15': [-150.4193093360257, -4354.553941197428],
    '2.20': [-156.951738116609, -4574.677688146315],
    '2.25': [-163.62289182855804, -6298.916390705273],
    '2.30': [-170.44108103789853, -7578.005784463885],
    '2.35': [-177.39864013544124, -8875.066671349887],
    '2.40': [-184.49557241016748, -4535.062907555057],
    '2.45': [-191.7318811477288, -11659.094617312894],
    '2.50': [-199.09298014510415, -10755.825172161125],
    '2.55': [-206.6049784945809, -11525.85840825618],
    '2.60': [-214.25093312816216, -17113.765554830115],
    '2.65': [-222.04383010878155, -18098.681847023436],
    '2.70': [-229.96767794171546, -24853.94117247755],
    '2.75': [-238.03031440636883, -27485.311110493913],
    '2.80': [-246.25277581036121, -34379.50704524319],
    '2.85': [-254.58744889353292, -33071.92908227058],
    '2.90': [-263.07332137309277, -45854.348820485524],
    '2.95': [-271.69172904503455, -50059.63925401883],
    '3.00': [-280.44887734968853, -61728.23302391083],
    '3.05': [-289.3553528948012, -70436.97343087442],
    '3.10': [-298.40120672822417, -87599.86208015257],
    '3.15': [-307.57893192594634, -93913.88700325647],
    '3.20': [-316.89558730419924, -108474.67733844646],
    '3.25': [-326.3551500285391, -128154.00094143602],
    '3.30': [-335.95181262927014, -131351.78417079165],
    '3.35': [-345.68750509890083, -190778.33031898714],
    '3.40': [-355.5643931751449, -222761.28559525192],
    '3.45': [-365.5759621402045, -183872.28579208365],
    '3.50': [-375.73101101051077, -249656.93816781786],
    '3.55': [-386.0251977113146, -367198.8964434871],
    '3.60': [-396.45610101477814, -360931.52114838536],
    '3.65': [-407.0260095908083, -473333.6318079952],
    '3.70': [-417.734919051065, -392016.8004628948],
    '3.75': [-428.5828250051266, -594732.0304985815],
    '3.80': [-439.5724052117476, -695376.770199431],
    '3.85': [-450.69560882257315, -970580.9953580673],
    '3.90': [-461.9689337019155, -940521.2515581927],
    '3.95': [-473.3758782527628, -1354918.6769616674],
    '4.00': [-484.9160236577233, -1551321.4438187003],
    '4.05': [-496.6010594015245, -822188.0718580398],
    '4.10': [-508.43141067971504, -2254112.2445011423],
    '4.15': [-520.3884658417015, -2648173.7742961845],
    '4.20': [-532.4875845782938, -2268767.174713491],
    '4.25': [-544.7323063569539, -3722014.586893156],
    '4.30': [-557.1060883878584, -3396303.8430801113],
    '4.35': [-569.629091492088, -3707860.643558214],
    '4.40': [-582.2842451131987, -3477400.728056874],
    '4.45': [-595.0892292967396, -5850825.013875462],
    '4.50': [-608.0187914245165, -8667979.577643322],
    '4.55': [-621.0871304100367, -9548731.788678858],
    '4.60': [-634.2942392990549, -11798648.418130748],
    '4.65': [-647.6638081759495, -12710813.759512678],
    '4.70': [-661.1529604544477, -14096488.49558468],
    '4.75': [-674.7851473892981, -7701118.354738492],
    '4.80': [-688.5606160021888, -3689187.2682606736],
    '4.85': [-702.4710521661735, -22575664.687016807],
    '4.90': [-716.5205685854651, -17291688.921153773],
    '4.95': [-730.7091633429301, -35605167.35845618],
    '5.00': [-745.0368345189374, -43652751.26909485],
    '5.05': [-759.5035801913579, -55501567.229625866],
    '5.10': [-774.1093984355654, -66931675.030944444],
    '5.15': [-788.8542873244365, -64024173.90126189],
    '5.20': [-803.7382449283486, -45350358.55749921],
    '5.25': [-818.7612693151834, -111935995.62649846],
    '5.30': [-833.9233585503243, -43553370.415870935],
    '5.35': [-849.2245106966567, -172932549.22671384],
    '5.40': [-864.6647238145688, -82038486.54998411],
    '5.45': [-880.2386313028419, -202438686.73543],
    '5.50': [-895.9568649391804, -253741186.6693815],
    '5.55': [-911.8197095642024, -250247472.50604945],
    '5.60': [-927.8161471223641, -459219604.37348443],
    '5.65': [-943.9401317468887, -409402094.70925885],
    '5.70': [-960.2261739922623, -630000742.8021698],
    '5.75': [-976.6516610698718, -437336590.5364992],
    '5.80': [-993.2165960597363, -906583613.5351571],
    '5.85': [-1009.8840643246214, -866242073.849215],
    '5.90': [-1026.7210351988947, -1238265626.1430774],
    '5.95': [-1043.6908934314458, -70810428.6592028],
    '6.00': [-1060.7933275848507, -1461043788.0418036],
    '6.05': [-1078.054290201966, -2273547317.913013],
    '6.10': [-1095.4346902833322, -1347761961.4503157],
    '6.15': [-1112.9674694786463, -1880356637.0408258],
    '6.20': [-1130.6326070212613, -1277613104.398408],
    '6.25': [-1148.4087939145263, -128800393.53254463],
    '6.30': [-1166.3941760356104, -184985520.0293087],
    '6.35': [-1184.4621874713675, -115641918.19420575],
    '6.40': [-1202.690754863689, -58736099.20048243],
    '6.45': [-1221.0436944110072, -6857481448.459557],
    '6.50': [-1239.5580749420865, -4144616746.3397164],
    '6.55': [-1258.188940474616, -14448922619.395897],
    '6.60': [-1276.9741465236802, -4751115462.742588],
    '6.65': [-1295.8749244361325, -31660773.782735877],
    '6.70': [-1314.9783039657389, -4416285674.087121],
    '6.75': [-1334.1489845619922, -4869143691.753127],
    '6.80': [-1353.4826943267028, -791306452.6267986],
    '6.85': [-1372.9637705989896, -11774729127.902395],
    '6.90': [-1392.5671353159662, -224660527.34623444],
    '6.95': [-1412.2920694174602, -34409087539.793686],
    '7.00': [-1432.2337468523494, -1070041299.6184514],
    '7.05': [-1452.2451602467368, -1823739421.098745],
    '7.10': [-1472.4174903723479, -18473962.89699372],
    '7.15': [-1492.7380260802631, -5494727.979056967],
    '7.20': [-1513.174904333614, -123474514080.13083],
    '7.25': [-1533.769196502277, -5131608396.219698],
    '7.30': [-1554.5689558497754, -7932583649.345241],
    '7.35': [-1575.3563353612108, -618235755.5829861],
    '7.40': [-1596.3583878583372, -385769.93859951023],
    '7.45': [-1617.5092693396284, -2226438284.3847017],
    '7.50': [-1638.799393027514, -15381764117.339403],
    '7.55': [-1660.299474046081, -22702789636.6137],
    '7.60': [-1681.7769030664722, -4660616703.489439],
    '7.65': [-1703.4844928480422, -149893138.35856643],
    '7.70': [-1725.3208279758642, -18038666459.869164],
    '7.75': [-1747.3067696170208, -19667460211.547276],
    '7.80': [-1769.3350734128544, -2804793053.7078876],
    '7.85': [-1791.6745816924315, -16389095086.4253],
    '7.90': [-1814.0779802883728, -2145413334.642002],
    '7.95': [-1836.6094490271873, -595628312.2459732]
}

lec_list_one_three['137'] = {
    '0.10': [-2.241713349852539, -0.37123918994961796],
    '0.15': [-3.0711601037169327, -0.7330432945848999],
    '0.20': [-4.0403177472861325, -1.2498312092155255],
    '0.25': [-5.1486159644240015, -1.9270746487387884],
    '0.30': [-6.396653671611328, -2.7994656754416978],
    '0.35': [-7.7840500433007795, -3.870620643758792],
    '0.40': [-9.310284894570248, -5.176900512879009],
    '0.45': [-10.976382994715028, -6.717065644495312],
    '0.50': [-12.781292360262205, -8.551134063961861],
    '0.55': [-14.72614191422407, -10.61221463031288],
    '0.60': [-16.809452231875916, -13.048869979470412],
    '0.65': [-19.032172290830918, -15.840006062197768],
    '0.70': [-21.393484854440914, -18.942573250324354],
    '0.75': [-23.895741635404175, -22.489175229490524],
    '0.80': [-26.535099029892574, -26.41139299824846],
    '0.85': [-29.315055618403697, -30.33788024179256],
    '0.90': [-32.23368625650024, -35.64132041686594],
    '0.95': [-35.29201267388672, -40.67504566027331],
    '1.00': [-38.487548474358775, -46.83334089872769],
    '1.05': [-41.82448197237221, -52.50279061817384],
    '1.10': [-45.29844044685785, -60.368969412858036],
    '1.15': [-48.91247325111309, -68.04965593230426],
    '1.20': [-52.66811542305018, -76.44710430266342],
    '1.25': [-56.5590095512287, -85.52826626319421],
    '1.30': [-60.59167601428699, -95.30854411654256],
    '1.35': [-64.76195112247063, -106.108011485225],
    '1.40': [-69.07288801806678, -117.64939130644117],
    '1.45': [-73.5229991204783, -129.98236952810691],
    '1.50': [-78.10941443906269, -143.43177384484184],
    '1.55': [-82.8376801686698, -158.06766763638282],
    '1.60': [-87.70187974527865, -173.58245527357775],
    '1.65': [-92.71051776501592, -190.33701360912704],
    '1.70': [-97.85495024904827, -207.74507325282917],
    '1.75': [-103.13585979326862, -227.43776626546753],
    '1.80': [-108.56079499288674, -246.8078491252971],
    '1.85': [-114.12497186109528, -270.2652497913278],
    '1.90': [-119.82399700307546, -293.5784879562475],
    '1.95': [-125.66490273845393, -319.1455591463044],
    '2.00': [-131.64811012515355, -345.59963466628324],
    '2.05': [-137.77069472280215, -374.9716815432414],
    '2.10': [-144.01858521350738, -368.84767902700975],
    '2.15': [-150.4193093360257, -434.706230571559],
    '2.20': [-156.951738116609, -465.15089878531654],
    '2.25': [-163.62289182855804, -509.2664657107387],
    '2.30': [-170.44108103789853, -550.3582238238698],
    '2.35': [-177.39864013544124, -593.2118866094346],
    '2.40': [-184.49557241016748, -584.997623346134],
    '2.45': [-191.7318811477288, -685.9635767821237],
    '2.50': [-199.09298014510415, -721.6382033605305],
    '2.55': [-206.6049784945809, -762.8945805769293],
    '2.60': [-214.25093312816216, -846.8282707998015],
    '2.65': [-222.04383010878155, -898.4149687342907],
    '2.70': [-229.96767794171546, -977.0132324182676],
    '2.75': [-238.03031440636883, -1044.6454693039718],
    '2.80': [-246.25277581036121, -1121.932605418039],
    '2.85': [-254.58744889353292, -1185.2516660835297],
    '2.90': [-263.07332137309277, -1281.8059539756605],
    '2.95': [-271.69172904503455, -1366.8501434750742],
    '3.00': [-280.44887734968853, -1465.1446906771364],
    '3.05': [-289.3553528948012, -1560.3433014826444],
    '3.10': [-298.40120672822417, -1675.6792672172687],
    '3.15': [-307.57893192594634, -1779.7392506741567],
    '3.20': [-316.89558730419924, -1898.2493720590094],
    '3.25': [-326.3551500285391, -2028.5359471811314],
    '3.30': [-335.95181262927014, -2128.2605349365886],
    '3.35': [-345.68750509890083, -2315.416766304147],
    '3.40': [-355.5643931751449, -2468.880841474445],
    '3.45': [-365.5759621402045, -2571.54392783114],
    '3.50': [-375.73101101051077, -2767.543165403203],
    '3.55': [-386.0251977113146, -2991.190006149072],
    '3.60': [-396.45610101477814, -3151.1553436590434],
    '3.65': [-407.0260095908083, -3385.7389853178674],
    '3.70': [-417.734919051065, -3473.008981599431],
    '3.75': [-428.5828250051266, -3835.6222892574156],
    '3.80': [-439.5724052117476, -4053.5789240631216],
    '3.85': [-450.69560882257315, -4352.913059367407],
    '3.90': [-461.9689337019155, -4578.300255272512],
    '3.95': [-473.3758782527628, -4921.160195781905],
    '4.00': [-484.9160236577233, -5241.913316917128],
    '4.05': [-496.6010594015245, -5133.541907205528],
    '4.10': [-508.43141067971504, -5945.505964665393],
    '4.15': [-520.3884658417015, -6320.320721615302],
    '4.20': [-532.4875845782938, -6540.183736948331],
    '4.25': [-544.7323063569539, -7145.7601433699265],
    '4.30': [-557.1060883878584, -7405.677031862823],
    '4.35': [-569.629091492088, -7835.338946739568],
    '4.40': [-582.2842451131987, -8575.47963775761],
    '4.45': [-595.0892292967396, -8905.279247111452],
    '4.50': [-608.0187914245165, -9705.038114189865],
    '4.55': [-621.0871304100367, -10237.382052031277],
    '4.60': [-634.2942392990549, -10944.669257230265],
    '4.65': [-647.6638081759495, -11563.188675380201],
    '4.70': [-661.1529604544477, -12201.538872326071],
    '4.75': [-674.7851473892981, -11939.822968586415],
    '4.80': [-688.5606160021888, -13931.210608558562],
    '4.85': [-702.4710521661735, -14564.018969643399],
    '4.90': [-716.5205685854651, -15119.17597185862],
    '4.95': [-730.7091633429301, -16552.08253365381],
    '5.00': [-745.0368345189374, -17600.299516483792],
    '5.05': [-759.5035801913579, -18969.233517000685],
    '5.10': [-774.1093984355654, -20175.55337589532],
    '5.15': [-788.8542873244365, -21265.136293765798],
    '5.20': [-803.7382449283486, -21809.06130598842],
    '5.25': [-818.7612693151834, -24149.220169319622],
    '5.30': [-833.9233585503243, -25560.205936446153],
    '5.35': [-849.2245106966567, -27303.656260089283],
    '5.40': [-864.6647238145688, -26467.04558943464],
    '5.45': [-880.2386313028419, -30452.939757887667],
    '5.50': [-895.9568649391804, -33022.77190629304],
    '5.55': [-911.8197095642024, -34230.52092957581],
    '5.60': [-927.8161471223641, -37487.350933501366],
    '5.65': [-943.9401317468887, -39541.64768741748],
    '5.70': [-960.2261739922623, -42076.60720567845],
    '5.75': [-976.6516610698718, -42122.38454376883],
    '5.80': [-993.2165960597363, -47805.77069876427],
    '5.85': [-1009.8840643246214, -50839.448317917246],
    '5.90': [-1026.7210351988947, -53882.832487744985],
    '5.95': [-1043.6908934314458, -57344.10584487055],
    '6.00': [-1060.7933275848507, -60346.93678254899],
    '6.05': [-1078.054290201966, -65138.98907372872],
    '6.10': [-1095.4346902833322, -68775.55216233412],
    '6.15': [-1112.9674694786463, -71169.16783509994],
    '6.20': [-1130.6326070212613, -78018.79414596237],
    '6.25': [-1148.4087939145263, -78816.40489463322],
    '6.30': [-1166.3941760356104, -83312.76000507089],
    '6.35': [-1184.4621874713675, -95197.0597028577],
    '6.40': [-1202.690754863689, -99972.16401370999],
    '6.45': [-1221.0436944110072, -106168.94522949195],
    '6.50': [-1239.5580749420865, -103542.58124143361],
    '6.55': [-1258.188940474616, -122788.03049661449],
    '6.60': [-1276.9741465236802, -123703.38759984107],
    '6.65': [-1295.8749244361325, -131241.26405849657],
    '6.70': [-1314.9783039657389, -143133.91125855094],
    '6.75': [-1334.1489845619922, -150020.1985213185],
    '6.80': [-1353.4826943267028, -161692.76676009526],
    '6.85': [-1372.9637705989896, -172738.51709570864],
    '6.90': [-1392.5671353159662, -190498.7406145048],
    '6.95': [-1412.2920694174602, -195629.26608088342],
    '7.00': [-1432.2337468523494, -217688.92024134903],
    '7.05': [-1452.2451602467368, -220544.426049527],
    '7.10': [-1472.4174903723479, -247579.5407341871],
    '7.15': [-1492.7380260802631, -248998.0008365331],
    '7.20': [-1513.174904333614, -276537.7954400914],
    '7.25': [-1533.769196502277, -294504.37976954144],
    '7.30': [-1554.5689558497754, -309777.82952123514],
    '7.35': [-1575.3563353612108, -334001.10182815796],
    '7.40': [-1596.3583878583372, -335630.0249553971],
    '7.45': [-1617.5092693396284, -333958.56482821883],
    '7.50': [-1638.799393027514, -395542.1631632189],
    '7.55': [-1660.299474046081, -419472.6246837107],
    '7.60': [-1681.7769030664722, -464956.7587314119],
    '7.65': [-1703.4844928480422, -494294.3862139501],
    '7.70': [-1725.3208279758642, -513430.1170005252],
    '7.75': [-1747.3067696170208, -545079.8609863316],
    '7.80': [-1769.3350734128544, -542490.5978926112],
    '7.85': [-1791.6745816924315, -641379.6325925401],
    '7.90': [-1814.0779802883728, -654124.0220895204],
    '7.95': [-1836.6094490271873, -725606.0959295218],
    '8.00': [-1859.2911947148484, -798485.6111650504],
    '8.05': [-1882.192316717482, -823988.525369449],
    '8.10': [-1905.0492390275288, -914606.0097057819],
    '8.15': [-1928.1367054282755, -820259.981848548],
    '8.20': [-1951.3749996134175, -935841.532274496],
    '8.25': [-1974.7525351000006, -1028436.9209374409],
    '8.30': [-1998.3543755518874, -1121001.5956880809],
    '8.35': [-2021.91303642119, -1277512.6470035985],
    '8.40': [-2045.7081541411353, -1314304.749091948],
    '8.45': [-2069.629929586313, -1449233.262080319],
    '8.50': [-2093.716116354316, -1420220.404920518],
    '8.55': [-2117.9032078477176, -1655212.4550860892],
    '8.60': [-2142.2289526536383, -1448771.5006273044],
    '8.65': [-2166.7196916650173, -1817215.2846786932],
    '8.70': [-2191.296383777192, -1899476.0106773311],
    '8.75': [-2216.105420523033, -2165989.756348213],
    '8.80': [-2241.0001094707727, -2304186.518542362],
    '8.85': [-2266.0543978618553, -2453445.3538990775],
    '8.90': [-2291.2341524853646, -2669059.906279585],
    '8.95': [-2316.5529952419047, -2726923.126634054],
    '9.00': [-2342.0109252596644, -3101267.6877593882],
    '9.05': [-2367.6079416641223, -3023046.7633491284],
    '9.10': [-2393.3440435780512, -1037743.1011790149],
    '9.15': [-2419.219230121521, -3424434.725112316],
    '9.20': [-2445.226070665665, -4061158.5652435035],
    '9.25': [-2471.3793446482605, -3625563.8776085265],
    '9.30': [-2497.6792886892717, -4677604.972742796],
    '9.35': [-2524.110804897473, -4320966.763859713],
    '9.40': [-2550.6659034525373, -4795334.783558311],
    '9.45': [-2577.383247230127, -5248985.057402426],
    '9.50': [-2604.1765430238506, -4808618.736476851],
    '9.55': [-2631.2196699758256, -5870733.657443872],
    '9.60': [-2658.3707203232952, -6218420.732356386],
    '9.65': [-2685.6123974084326, -6860291.115873544],
    '9.70': [-2712.9926526116615, -7601791.224985818],
    '9.75': [-2740.5780692562025, -7757353.696071524],
    '9.80': [-2768.269765667835, -7770022.387456922],
    '9.85': [-2796.0752286305615, -8836658.436808543],
    '9.90': [-2824.0365771854636, -9526464.117499294],
    '9.95': [-2852.1456568979634, -10057435.18106757]
}

lec_list_one_four['137'] = {
    '0.10': [-2.241713349852539, 0.24569396477133967],
    '0.15': [-3.0711601037169327, 0.06780166792113267],
    '0.20': [-4.0403177472861325, -0.22336628400193362],
    '0.25': [-5.1486159644240015, -0.6418627575363183],
    '0.30': [-6.396653671611328, -1.207229180756135],
    '0.35': [-7.7840500433007795, -1.929044130968416],
    '0.40': [-9.310284894570248, -2.827620414818295],
    '0.45': [-10.976382994715028, -3.9102053241603847],
    '0.50': [-12.781292360262205, -5.208152933930167],
    '0.55': [-14.72614191422407, -6.695893252149921],
    '0.60': [-16.809452231875916, -8.449610181550119],
    '0.65': [-19.032172290830918, -10.460918170074276],
    '0.70': [-21.393484854440914, -12.715103143793295],
    '0.75': [-23.895741635404175, -15.28124179705932],
    '0.80': [-26.535099029892574, -18.129402255937986],
    '0.85': [-29.315055618403697, -21.110777779186705],
    '0.90': [-32.23368625650024, -24.811331646829313],
    '0.95': [-35.29201267388672, -28.556473213232344],
    '1.00': [-38.487548474358775, -32.88675978078561],
    '1.05': [-41.82448197237221, -37.18182654521661],
    '1.10': [-45.29844044685785, -42.563973127132414],
    '1.15': [-48.91247325111309, -48.0290012696559],
    '1.20': [-52.66811542305018, -53.9782103635785],
    '1.25': [-56.5590095512287, -60.365289914660195],
    '1.30': [-60.59167601428699, -67.24958664961711],
    '1.35': [-64.76195112247063, -74.7305044428001],
    '1.40': [-69.07288801806678, -82.72226549846859],
    '1.45': [-73.5229991204783, -91.23085929287275],
    '1.50': [-78.10941443906269, -100.40194950602833],
    '1.55': [-82.8376801686698, -110.27729118706151],
    '1.60': [-87.70187974527865, -120.7308018335645],
    '1.65': [-92.71051776501592, -131.91760944729117],
    '1.70': [-97.85495024904827, -143.6517754321499],
    '1.75': [-103.13585979326862, -156.4125102835575],
    '1.80': [-108.56079499288674, -169.39198842372255],
    '1.85': [-114.12497186109528, -184.1939644541464],
    '1.90': [-119.82399700307546, -199.25958573485778],
    '1.95': [-125.66490273845393, -215.36946631824233],
    '2.00': [-131.64811012515355, -232.28678410831856],
    '2.05': [-137.77069472280215, -250.41612122065087],
    '2.10': [-144.01858521350738, -255.65600692664455],
    '2.15': [-150.4193093360257, -288.35072339492694],
    '2.20': [-156.951738116609, -308.14575940583416],
    '2.25': [-163.62289182855804, -332.65301896098657],
    '2.30': [-170.44108103789853, -356.71533762799464],
    '2.35': [-177.39864013544124, -381.78177399075315],
    '2.40': [-184.49557241016748, -391.62301366354393],
    '2.45': [-191.7318811477288, -435.7998867514885],
    '2.50': [-199.09298014510415, -460.1504088638299],
    '2.55': [-206.6049784945809, -485.8214808789162],
    '2.60': [-214.25093312816216, -527.2585900399029],
    '2.65': [-222.04383010878155, -558.1888066284839],
    '2.70': [-229.96767794171546, -597.7644066437779],
    '2.75': [-238.03031440636883, -634.9285914413944],
    '2.80': [-246.25277581036121, -675.2831705527178],
    '2.85': [-254.58744889353292, -712.9749622772458],
    '2.90': [-263.07332137309277, -759.5331550233102],
    '2.95': [-271.69172904503455, -804.3351878899255],
    '3.00': [-280.44887734968853, -853.3416954563234],
    '3.05': [-289.3553528948012, -902.0600991087048],
    '3.10': [-298.40120672822417, -957.643233654882],
    '3.15': [-307.57893192594634, -1010.7324489701904],
    '3.20': [-316.89558730419924, -1068.897171518097],
    '3.25': [-326.3551500285391, -1130.2536297653742],
    '3.30': [-335.95181262927014, -1184.9143497055159],
    '3.35': [-345.68750509890083, -1263.3303912448123],
    '3.40': [-355.5643931751449, -1333.9715699025678],
    '3.45': [-365.5759621402045, -1393.1947631327914],
    '3.50': [-375.73101101051077, -1476.393965532213],
    '3.55': [-386.0251977113146, -1566.9390862602397],
    '3.60': [-396.45610101477814, -1643.415504661974],
    '3.65': [-407.0260095908083, -1739.507401826987],
    '3.70': [-417.734919051065, -1801.8097113140495],
    '3.75': [-428.5828250051266, -1930.1261600319046],
    '3.80': [-439.5724052117476, -2026.4468064997752],
    '3.85': [-450.69560882257315, -2140.0086710637593],
    '3.90': [-461.9689337019155, -2244.5585955303422],
    '3.95': [-473.3758782527628, -2367.7141410375266],
    '4.00': [-484.9160236577233, -2493.307704302547],
    '4.05': [-496.6010594015245, -2525.0002007697344],
    '4.10': [-508.43141067971504, -2759.455556383797],
    '4.15': [-520.3884658417015, -2899.9968046907384],
    '4.20': [-532.4875845782938, -3003.70732196558],
    '4.25': [-544.7323063569539, -3202.4658014423994],
    '4.30': [-557.1060883878584, -3321.7158956392054],
    '4.35': [-569.629091492088, -3483.5810812080285],
    '4.40': [-582.2842451131987, -3708.369390612675],
    '4.45': [-595.0892292967396, -3849.6856207695746],
    '4.50': [-608.0187914245165, -4090.154079813979],
    '4.55': [-621.0871304100367, -4280.123677728194],
    '4.60': [-634.2942392990549, -4504.403433468597],
    '4.65': [-647.6638081759495, -4716.269816698713],
    '4.70': [-661.1529604544477, -4929.657942871455],
    '4.75': [-674.7851473892981, -4967.530728516833],
    '4.80': [-688.5606160021888, -5455.255073805364],
    '4.85': [-702.4710521661735, -5675.8949933889535],
    '4.90': [-716.5205685854651, -5890.455735825737],
    '4.95': [-730.7091633429301, -6254.118384556076],
    '5.00': [-745.0368345189374, -6557.178965283885],
    '5.05': [-759.5035801913579, -6929.894304470142],
    '5.10': [-774.1093984355654, -7266.275006825581],
    '5.15': [-788.8542873244365, -7584.459179623853],
    '5.20': [-803.7382449283486, -7841.887032943189],
    '5.25': [-818.7612693151834, -8349.645910713225],
    '5.30': [-833.9233585503243, -8745.569394456239],
    '5.35': [-849.2245106966567, -9170.93938709418],
    '5.40': [-864.6647238145688, -9177.40475360211],
    '5.45': [-880.2386313028419, -10007.599876135591],
    '5.50': [-895.9568649391804, -10589.15958095068],
    '5.55': [-911.8197095642024, -10962.69375602344],
    '5.60': [-927.8161471223641, -11649.057915324445],
    '5.65': [-943.9401317468887, -12175.72603542247],
    '5.70': [-960.2261739922623, -12748.312515175456],
    '5.75': [-976.6516610698718, -12940.786696281431],
    '5.80': [-993.2165960597363, -14017.48595234578],
    '5.85': [-1009.8840643246214, -14683.113351230124],
    '5.90': [-1026.7210351988947, -15364.282408262588],
    '5.95': [-1043.6908934314458, -16104.349278664924],
    '6.00': [-1060.7933275848507, -16781.34388115216],
    '6.05': [-1078.054290201966, -17668.68778765861],
    '6.10': [-1095.4346902833322, -18428.847108108377],
    '6.15': [-1112.9674694786463, -19133.88263855518],
    '6.20': [-1130.6326070212613, -20293.278184467847],
    '6.25': [-1148.4087939145263, -20667.855538402855],
    '6.30': [-1166.3941760356104, -21853.08697589395],
    '6.35': [-1184.4621874713675, -23402.399425899384],
    '6.40': [-1202.690754863689, -24338.226254953704],
    '6.45': [-1221.0436944110072, -25470.413809121743],
    '6.50': [-1239.5580749420865, -25611.5485914641],
    '6.55': [-1258.188940474616, -28202.10015820703],
    '6.60': [-1276.9741465236802, -29032.238960048155],
    '6.65': [-1295.8749244361325, -30189.741089317053],
    '6.70': [-1314.9783039657389, -31923.32230717716],
    '6.75': [-1334.1489845619922, -33460.63797443802],
    '6.80': [-1353.4826943267028, -35026.99641639878],
    '6.85': [-1372.9637705989896, -36697.09757897393],
    '6.90': [-1392.5671353159662, -38952.574417777236],
    '6.95': [-1412.2920694174602, -40089.79431130463],
    '7.00': [-1432.2337468523494, -42881.222283674295],
    '7.05': [-1452.2451602467368, -43932.67912807587],
    '7.10': [-1472.4174903723479, -47048.76029244798],
    '7.15': [-1492.7380260802631, -48228.57779475267],
    '7.20': [-1513.174904333614, -51252.23036450703],
    '7.25': [-1533.769196502277, -53717.854231213765],
    '7.30': [-1554.5689558497754, -56067.87010401913],
    '7.35': [-1575.3563353612108, -58730.33205892598],
    '7.40': [-1596.3583878583372, -60695.41149600043],
    '7.45': [-1617.5092693396284, -60542.98193195747],
    '7.50': [-1638.799393027514, -66938.61575810623],
    '7.55': [-1660.299474046081, -70609.96130114186],
    '7.60': [-1681.7769030664722, -74741.51935323304],
    '7.65': [-1703.4844928480422, -77816.52811378888],
    '7.70': [-1725.3208279758642, -81013.57548678745],
    '7.75': [-1747.3067696170208, -84760.30971278471],
    '7.80': [-1769.3350734128544, -85670.35364247231],
    '7.85': [-1791.6745816924315, -94048.0229269554],
    '7.90': [-1814.0779802883728, -97080.11907713732],
    '7.95': [-1836.6094490271873, -103162.99253223822],
    '8.00': [-1859.2911947148484, -109364.48920183828],
    '8.05': [-1882.192316717482, -112798.59338529922],
    '8.10': [-1905.0492390275288, -120247.3952557208],
    '8.15': [-1928.1367054282755, -116368.1026097815],
    '8.20': [-1951.3749996134175, -127789.04168193937],
    '8.25': [-1974.7525351000006, -133544.97838286828],
    '8.30': [-1998.3543755518874, -141038.8738020222],
    '8.35': [-2021.91303642119, -152322.4957395722],
    '8.40': [-2045.7081541411353, -157450.76348026047],
    '8.45': [-2069.629929586313, -167102.38142946348],
    '8.50': [-2093.716116354316, -168267.2212592723],
    '8.55': [-2117.9032078477176, -183952.3194092704],
    '8.60': [-2142.2289526536383, -176856.7967405334],
    '8.65': [-2166.7196916650173, -197948.02389779233],
    '8.70': [-2191.296383777192, -206939.47843606496],
    '8.75': [-2216.105420523033, -222340.62703177085],
    '8.80': [-2241.0001094707727, -233286.80375319172],
    '8.85': [-2266.0543978618553, -243718.9963263235],
    '8.90': [-2291.2341524853646, -256547.80293468013],
    '8.95': [-2316.5529952419047, -265674.2573305992],
    '9.00': [-2342.0109252596644, -284551.8590283541],
    '9.05': [-2367.6079416641223, -289430.5348056311],
    '9.10': [-2393.3440435780512, -309627.0630166979],
    '9.15': [-2419.219230121521, -311255.46793141833],
    '9.20': [-2445.226070665665, -345503.467857891],
    '9.25': [-2471.3793446482605, -341692.6354408342],
    '9.30': [-2497.6792886892717, -379611.78003355203],
    '9.35': [-2524.110804897473, -374915.1583100813],
    '9.40': [-2550.6659034525373, -398498.56223092065],
    '9.45': [-2577.383247230127, -422749.18968259083],
    '9.50': [-2604.1765430238506, -457523.2039577933],
    '9.55': [-2631.2196699758256, -462433.63668152184],
    '9.60': [-2658.3707203232952, -478855.0125263103],
    '9.65': [-2685.6123974084326, -505715.8636087981],
    '9.70': [-2712.9926526116615, -541370.1760344201],
    '9.75': [-2740.5780692562025, -561057.3098265716],
    '9.80': [-2768.269765667835, -579154.9627222668],
    '9.85': [-2796.0752286305615, -613609.7298907933],
    '9.90': [-2824.0365771854636, -642409.6178257633],
    '9.95': [-2852.1456568979634, -681575.9380672561]
}

lec_list_c[
    '450'] = {  #                            E_pp=12    a_pp=7.766    a_pp=3.0
        '2.00':
        [-163.71595, -157.447133, 157.961, -3.267336, 39.607794, -7.87235],
        '4.00':
        [-483.66597, -473.014504, 837.417, -9.154840, 70.028319, 8.869022],
        '6.00':
        [-974.12019, -959.080826, 2710.51, -16.53103, 98.155928, 17.98276],
        '8.00': [
            -1635.0553, -1615.626551, 7181.98, -24.93847, 124.958616, 26.50637
        ],
        '10.0': [
            -2466.4663, -2442.646318, 17329.9, -34.22299, 150.757077, 34.34971
        ],
        '12.0': [
            -3468.3515, -3440.139992, 40042.8, -44.21432, 175.702462, 37.62653
        ],
        '15.0': [
            -5290.8112, -5256.012203, 136994.4343, -60.31870, 211.985648,
            45.16885
        ]
    }

lec_list_c['805'] = {  #                       E_pp=15   a_pp=3.0
    '2.00': [-148.020, -138.168, 71.0200, -2.125143, 6.908400],
    '4.00': [-404.629, -388.507, 353.8714, -6.886135, 31.56619],
    '6.00': [-789.207, -766.806, 1001.2247, -12.97822, 47.92537],
    #'6.00': [-974.12019, -959.080826, 2710.51, -12.97822, 47.92537],
    '8.00': [-1301.721, -1273.037, 2220.7696, -20.06991, 63.65185],
    '10.0': [-1941.969, -1907.003, 4307.9937, -28.14412, 77.47199],
    '12.0': [-2710.252, -2668.999, 7711.9141, -36.76308, 91.74684],
    '15.0': [-4102.503, -4051.821, 16837.2070, -50.77141, 113.9574]
}

lec_list_oneMEV_orig['137'] = {  #d0GS TNI-UIX  ZENTRAL NNN   PROJ           d0ES
    '0.05': [-1.551665, 0.324253617188],
    '0.10': [-2.241663, 0.2456829375],
    '0.16': [-3.25382381543, 0.0190507091372],
    '0.20': [-4.040227, -0.223247242969],
    '0.22': [-4.46682689578, -0.374771360196],
    '0.25': [-5.14850032428, -0.641645783435],
    '0.30': [-6.396510, -1.20682104512],
    '0.35': [-7.8083, -1.98064161217],
    '0.40': [-9.31007578154, -2.82776987047],
    '0.45': [-10.9761364604, -3.91309051448],
    '0.50': [-12.78163, -5.20893734689],
    '0.55': [-14.7258111587, -6.71792212184],
    '0.60': [-16.8090746843, -8.46827168904],
    '0.65': [-19.03174482, -10.4630055535],
    '0.70': [-21.39405, -12.7344455911],
    '0.75': [-23.8940370852, -15.2760761543],
    '0.80': [-26.53580, -18.1374520182],
    '0.90': [-32.23375, -24.8126425911],
    '0.95': [-35.29122, -28.6644794764],
    '1.00': [-38.48853, -32.9110143276],
    '1.05': [-41.82441, -37.5268116221],
    '1.10': [-45.29949, -42.5703870486],
    '1.20': [-52.66596, -53.9705109645],
    '1.50': [-78.11106, -100.476136019],
    '2.00': [-131.64598, -232.412644337],
    '3.00': [-280.45691, -854.107499493],
    '4.00': [-484.92093, -2495.36419052],
    '6.00': [-1060.7967, -16915.6302127],
    '10.0': [-2880.3865, -588383.449462234]
    # TNI below is fitted to B(3) = 8.48
    #'10.0': [-2880.3865, -29933.4954397]
}

lec_list_c['137'] = {  #d0GS TNI-UIX  ZENTRAL NNN   PROJ           d0ES
    '2.00':
    [-142.364, -106.2793, 68.488, 66.8240, 33.4723, -276.2272, -0.830307],
    '4.00':
    [-505.164, -434.9584, 677.799, 724.4771, 338.7663, -892.3704, -7.645753],
    '6.00': [
        -1090.584, -986.2518, 2652.651, 3198.9831, 1355.3977, -1692.1660,
        -16.854889
    ],
    '8.00':
    [-1898.622, -1760.1617, 7816.228, 0.0, 4101.7017, -2539.0099, -27.502527],
    '10.0': [
        -2929.277, -2756.6884, 20483.217, 0.0, 11095.8257, -3328.0227,
        -39.169742
    ],
    '12.0': [
        -4182.363, -3975.6195, 50939.941, 0.0, 28724.6969, -3999.5813,
        -52.024708
    ],
    '15.0': [
        -6479.576, -6221.5028, 195570.801, 0.0, 118778.9520, -4694.7019,
        -71.996883
    ]
}

w120 = [
    129.5665, 51.3467, 29.47287, 13.42339, 8.2144556, 4.447413, 2.939,
    1.6901745, 1.185236, 0.84300, 0.50011, 0.257369, 0.13852, 0.071429,
    0.038519, 0.018573, 0.0097261, 0.00561943, 0.002765, 0.00101
]
w12 = [
    12.95665, 5.13467, 2.947287, 1.342339, .82144556, .4447413, 2.939,
    1.6901745, 1.185236, 0.84300, 0.50011, 0.257369, 0.13852, 0.071429,
    0.038519, 0.018573, 0.0097261, 0.00561943, 0.002765, 0.00101
]

mn = {
    '137': 938.91852,
    '300': 1053.0,
    '450': 1226.0,
    '510': 1320.0,
    '805': 1634.0
}