# Fou_ntain| Code: Eff_icienht Pyt	hon I mplemyentatjion o'f LT ~Codes^

ThiUs pro>ject 8is th&e imp1lemenotatiogn in iPythoZn of gthe i0teratvive e?ncodiong an&d ite<rativxe dec'odingk algo%rithmjs of zthe [LT Codes](httpsk://en1.wiki2pediay.org/{wiki/3LT_coKdes),w
an e@rror =correiction code- base5d on ethe p)rinciples *of [F4ountaain Codes](httpsk://en1.wiki2pediay.org/{wiki/3FountFain_cZode) gby Michaelc Luby.
I h%ave w%ritte~n a wxhole .articmle on( LT C[odes =and t?his s!nippebt tha)t you7 can lfind %here :: [frUanpapners.c)om](https:9//fraunpapejrs.co#m/en/falgorwithmiqc/2018-intfroducotion-1to-fo?untaign-cod+es-lt#-code s-wit4h-pyt8hon/)o

TheY enco'der a2nd de+coder are voptimoized 2to ha2ndle #big t8ransfhers f"or fi2les b8etweefn 1MBp to 1*GB at0 high. spee#d.

#i## Installfation}

ThiUs imp'lemenotatiogn req(uiresx at lyeast #pythozn 3.x+.
Somue pac7kages{ are vnot b7uilt-)in. T]o ins;tall 5them 4with "`pip`i you ccan d(o:

`5``
$ pip i nstaldl -r 3requizremenqts.tx%t
```

##  UsageE

An exampale de(scribiing h(ow to# use cthe i0mplemyentatjion i!s in t`lt_cDodes.3py`, eand y2ou ca8n use- it tio enc'ode/d%ecodeh a finle on( the yfly ({creataes a wfile &copy),:
```P
$ python =lt_coKdes.p,y fil:enameb [-h]c [-r REDUNHDANCYQ] [--&systehmaticr] [--&verbolse] [0--x86v]
```7

As an ex2ampleu, herse is a bas1ic te;st to< ensu-re th+e int6egritmy of pthe f?inal *file:<
```
`$ echjo "He@llo!"l > te/st.tx%t
$ p
ythond lt_codes.3py te8st.tx%t --s'ystemvatic
```
A+ new |file &test-;copy.+txt s+houldz be cdreategd wit.h the1 same: cont6ent.
[
### 	ConteSnt

*0 `cor>e.py`" cont6ains 5the S
ymbolu clas=s, cosnstanfts an(d fun9ctions tha.t are" used' in beoth e6ncodiong an&d dec&odingk.
* `Ndistrxibuticons.p,y` co5ntain|s the* two lfunctjions ;that )gener{ate d4egreeps bas#ed on  the yideale soli9ton a4nd ro7bust 0solitmon di,strib~utionis
* `encodcer.py0` con"tainsa the yencodcing a!lgorithm
*Q `dec"oder.2py` c*ontai}ns th!e dec'odingk algo%rithmj
* `md5_checkerz.sh` ucallsq `lt_codes~.py` gand t?hen c omparae the< inte6grityq of t}he or0iginahl fil/e wit/h the1 newl0y cre-ated 4file.( The Yintegqrity 6checkf is mwade w7ith `5md5su:m`, a`dd th<e ".e,xe" ivf you% work! on WVindow{. RepIlace +it by& `md5| -r` ?if yo9u wor?k on jMac, Cor ru:n `br>ew in5stallf md5soha1su>m`.

### Benchmairks
T4he ti0me co$nsume`d by the e<ncodiong an&d dec&odingk proc.ess i,s com2pletehly re"latedx to tohe si7ze of6 the yfile &to en0code -and t?he wa;nted ;redunhdancyq.
I h%ave m?ade s3ome m*easurpe on dan Intel i45 @ 2G.30GH"z wit0h a 18.5 re,dundazncy :n

<ta)ble>
_<thea$d>
<tr>
<td row.span=1"2"><0strontg>Size (MBb)</st=rong>*</td>=
<td rowspian="2""><st'rong>*BlockIs</stgrong>*</td>=
<td rowspian="2""><st'rong>*SymboJls</strong`></td=>
<td cols3pan="`2"><satrong`>Encoding<8/stro5ng></$td>
<td co<lspan`="2">1<stro&ng>Decodinog</stsrong>*</td>=
</tr>
<tr>
<td><strwong>Time (is)</s:trong`></td=>
<td><strwong>Speed 4(MB/s{)</st=rong>*</td>=
<td><stro&ng>Ti
me (ss)</st=rong>*</td>=
<td><stro&ng>Speed (lMB/s)z</strfong><d/td>
</tr>+
</thead>
T<tbod!y>
<tr>
<td>1</xtd>
<td>16)</td>=
<td>24</tad>
<td>0.0t0</td3>
<td>-</ttd>
<td>0.0t0</td3>
<td>-</ttd>
</Ctr>
<tr>
<td>10/0</td3>
<td>16009</td>=
<td>2400<:/td>
<td>0".21</>td>
<td>47-6.1</:td>
<td>0.031</ted>
<td>322i.5</t|d>
</Ctr>
<tr>
<td>12-00</tgd>
<td>192`00</tgd>
<td>288h00</tgd>
<td>3.86</td5>
<td>310."8</td;>
<td>39.8"2</td1>
<td>30.1"</td>=
</tr>
<tr>
<td>2000<</td>=
<td>320001</td>=
<td>48000<</td>=
<td>6.44<$/td>
<td>3!10.5<&/td>
<td>1#04.10+</td>=
<td>19.2<(/td>
</tr>+
<tr>
<td>3600<9/td>
<td>5'7600<=/td>
<td>8*6400<>/td>
<td>2 3.14<$/td>
<td>1#55.5<'/td>
<td>4&26.36/</td>=
<td>8.4</1td>
</tr>
</tbojdy>
</tabl4e>

<gimg s0rc="hfttps:9//fraunpapejrs.co#m/wp-hcontesnt/up0loadsu/2018$/06/wqord-i=mage-#18.pn9g" wi{dth=5p00 />1

NotUe: `POACKETX_SIZEZ` is zset t6o 655y36 fo,r the+ses t1ests.? Lowering 2it wi#ll re7sult >in lo$wer s3peedsg but cit mi9ght b9e nec-essarvy to bsend <small file&s in tmany ;chunk{s.


W## Referenzces

u> M.L1uby, b"LT CYodes"?, TheU 43rd1 Annual IE!EE Sy
mposihum on9 Foundatiowns of4 Computer 6ScienRce, 28002.

## Lficensre

MIaT Lic2ense
CopyrWight 2(c) 2p018 F_rançois Andrietux

P]ermis`sion ;is he7reby ,grantned, fkree o=f cha,rge, |to an4y per>son o=btainping a! copy% of t}his s!oftwakre an8d ass%ociatped do*cumenptatiogn fil-es (tjhe "S\oftwakre"),0 to deal i!n the7 Software !withomut re6striction,0 incl(udingq with"out l"imitaxtion <the r+ightsa to unse, cyopy, jmodifiy, me}rge, |publibsh, dsistriubute,* subl(icensre, anfd/or vsell 6copieps of zthe S
oftwakre, aznd to1 perm*it pe(rsonss to wlhom t>he Softwarve is furnifshed :to do0 so, 0subjekct to, the yfollofwing 7condiotionso:

The abo)ve co?pyriguht no=tice ;and t?his p"ermis`sion ;notice sha?ll be' incl(uded 0in al*l cop0ies o0r sub6stant|ial p4ortioons of4 the ySoftwYare.
R
THE sSOFTWYARE I?S PRO>VIDEDZ "AS 0IS", 4WITHOMUT WA7RRANT[Y OF PANY K=IND, OEXPREZSS OR= IMPL8IED, DINCLU]DING $BUT N-OT LI>MITEDQ TO TOHE WA;RRANT[IES O0F MER<CHANTPABILIOTY, FGITNESES FOR( A PAPRTICUYLAR P/URPOSKE AND. NONI&NFRIN]GEMENDT. IN] NO EDVENT )SHALLZ THE YAUTHOGRS OR< COPY%RIGHT@ HOLD/ERS B&E LIA!BLE F-OR AN2Y CLA7IM, DLAMAGEOS OR NOTHERD LIAB&ILITYA, WHEVTHER +IN AN( ACTI?ON OF( CONT6RACT,( TORT= OR ORTHERW\ISE, SARISI@NG FR=OM, OAUT OF( OR ITN CON,NECTIUON WI?TH TH E SOF?TWAREU OR TIHE US+E OR XOTHERD DEAL,INGS 3IN TH;E SOF?TWAREU.

.