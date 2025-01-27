import networkx as nx

from aoc_lib import solve_problem

INPUT = """qtf: xjk
hqq: zqg fhv rkr kgm mfk gzl
xmp: bvj
bph: tjs cbv kjp
lxr: rpt sht ckx
klg: clv lql lht
sjl: ghv dqv
zfg: pql
nzq: grq
hmp: lsh mht zmq xbt qhl
rfv: hth jlj mst pkh
xzq: pcj
hmt: krb dgp
bkk: jsf
pxz: spk fxr
pjc: vpl sjk
lvd: cnm qzd
tdm: qhm
nrq: thg qjf dgr
qgp: lgg qnb gcb sbs
zmp: xdn
cjp: zzt dtg rvq
tzd: xxl szf
rvc: gtc
ztn: bsq
jkv: vkn tnq
jss: prg
htc: rhb
jzx: qst qkp
zjj: thg
xrs: zmt rkr
nxd: sdb pxp rcb
tmz: xxl
lzd: mbv hth llq fvk rgp
nbp: dkz lht
nfm: kqz kjp xpc
cfj: mnl rlm
lxj: pxz hdg bpz zzk
pmq: fbh chq xql fdr khz
rhb: dvl
bhc: qml nvz bzl qkh
frt: qrg rtj dcx cnm qkl
grj: nqr rpt clp qsr
vqh: qhl
dtm: kfx
mgs: ksn cbd chq jnt
jpq: lcl gxb
ncz: lmh
tkz: nnb qrh dgc spk
zfz: cmz
dcx: jkh kjd htc pgs
jdd: klc jmg fzp zkb
jqz: hfz
ncq: kfn xbj
gdd: bhv kjd
ldh: ntr
gjq: rpt nvv mgk cbx
zkx: jbr
vqj: prg dlk
kcz: xbt dhq
vcs: cpz vpz szf
klh: gjj rss frx gsl
dmm: bkt ftg fbg rfl shq
qrz: dlk
nss: gnc tsn
qrt: mnf trz vlh
jqx: rtr lvd ktl
csj: mvp rgh srv sxz cqg
cps: snh jdr nmr czr nfb
sll: spv lzh mrj sjz
bld: bgj qsr xgm
vjm: tzq fcl fbt
jdr: tkr hkr nch
kbm: zlx
xcn: vrs spf
ndl: trq bmn jqz
nvz: gjd rlr pgz
hsm: dzq
rbg: jhg
rgh: lcz pkr jtn tvs
zzt: phl
vkn: kkq vhz
kbl: ftt
lpn: snt spk kpd mnh xrp jqc
bvs: tkn kqg jzf vjp
nft: bhq
glf: sxv cgp sqb
bqg: mqh kqb
rsl: kqs krg mmb gql kkq
dzn: trb zmq rzs
mhr: rtb grf bcq lsc
pxh: xrx
csc: jkh jpk brx tvm cgc
vnb: gcq rvc sfb
jlt: pbd grq
gdk: lkc flf kvd lds
bmk: dzp ncj jkh hzs
svl: llp sjz pfp xpm
cxb: cxv sfb zbt
qlb: jsp
vkv: pcj
knd: ttj kzj zmq
tnt: jkv tzd bxz bch
fdp: hfg rrq fxl
fhb: krp vsp mht
mgd: zrq pkr
mtp: xzz trb lpb
gcl: nkj gst njc fcr xrn mzp
pjk: ttj mnh dtg
pts: sjk dxr hkx
qlm: hsv hnv
zrr: fqh
rkz: xqg cxf jqp
nml: gjc ncq ngm hdq
zpv: zkx
rtv: vpz rlm
nkk: clp mrn
rxm: tdl vhq vqh
cjs: kcc rsl nhh
scc: cjv bbk jpk vpz xmx
nct: rhp
xvd: mqn dht tvh kxz rxj
kth: snl
trl: bqd rrs jgt
ksn: nft
bhb: ncd bxk qsj rtj qtz
sfj: zqx vgp mgk
xdf: ccc fgt rgp
dkh: vzm
mmc: vxm
hmd: klp rdj kjm
djd: fhf cqc xxl rfm
sql: tkj drb rhb
lzm: ttt bhv dtm lbm
mrj: jnv krz qll
bmf: hls
mkf: kqb psb fff dkp
bxz: hfq ckt
ltx: sfn hmt xmv
vgc: tbs xjk nrm
rps: gtj lbm qzx jvt
dzb: rfp bpv dbj dtg
qjc: psg zfz dzq hfp
bns: ccr jkp
tdh: bqm jtz nnc brh
pxd: mpq nmq tzd hfg
jvt: lhr
rmd: rjf hgz zgd ckz
spg: gxh ltx rhb
dhp: vlg ppt gnn
tnq: fld
vhj: dsg ckh nrk rmc
gqb: mbr pmd qtk rzg
gzh: gcm
dht: sdm
hjg: jcr fxx rdj xfm llf
kff: bnl
rpq: nkc tdp dks
smh: mpn lkh
gnn: mph rxm
zzn: plq bcc
str: csq xtk gff
lgg: xdj lsc mkt
qfn: gxh
xzg: zpm tnn vmc bkd qkj
gxd: rbg qtz mjc vzp
vbc: sxj cgn
fkm: xrx tnt sqg
dgv: tvg
dfj: xqg
vmb: vdn tjs kdc lkh hgt
gjc: vpl prg nrq
tcx: drg
sgd: plm jsp vrs
kjn: vjs pbx jnt
njs: szx vfq gff
xbm: lbf ftg ngm zgv
ksc: ggp mjz cpt llx ljk
zmz: ljm ddv gbl cgc
jpz: bkb drb vgs hkc
vpz: ntr
ptb: bln xpf crb
tns: pbd
tvp: fdh kvm
mkt: kck ntv ksl gcs
dkp: fff bxg
bbs: slm tnn cmr fhq
tph: tzs zpm rmf
mph: zqx scz sxj zjj
djg: lnn
kvg: zkj xrp ktv
rgv: vgv cmg
kzb: rqk clv csj mhx
chf: bvj lhp nct
bln: zfj
dlv: tqp jqv xjz rbz
mbh: fbt mlf
jmg: lpk
dcm: rxv mpn zfz
qqt: sgp cnm brx drt
gzg: zqn gxb gjj qpz
fdh: frf
fmx: dqt rzb nzc
jnf: ptr mjb
mhs: ffr
ltn: lzv
vpn: rtv jst
qqp: fhq pjc zpv hpf
txt: kbm snr
dpv: bld ggl pdd qsn
jpk: blf jsp
gzl: tqz sgd vbn
xxn: mrr tjs jbf lkh
pll: vck jnq vjp
qkh: vls hsd hxj ktg mff
rxl: kmz qtk pxh
jrh: jtz vls
pnl: mbr nrm rrq mfh
hsb: hfz
nhc: spf bbk rrt
gcv: tcx hmt lln bjh
bgd: zlx
rms: rbg fxf blf mlc spg
qbx: vgj
zkh: qsr lsh xbt qcm ncz
mmx: rtj xql bcc xgl
gkz: gnc zqv
jsg: fts mds
qjf: psh jjt
lbf: nsq
htl: nlv
ttb: ckb dvl
xjc: pxh rfn jqv
krg: zvm
zct: kfq xtv qkh fkp
hvz: tgn plq vcn
jbb: clp fgt ssv
qrh: lmh rns
gns: nsr gqb mqc htc
fxj: djc zfj dfg grn
rpt: cpt cbj
zrh: hgl hgr dbl zvv
dhh: tzs qbf
dkz: tzt xtf qlb
gbn: fxr
trj: rfk vjl
qfm: mkb bqm bch tqz
nfk: kbz bsq hpk
sxz: hqb
drz: vlt
dbs: kzz
bcg: qdp lhk zjq jsf
psb: cmz ltn fch
kjh: dsf xdn
flg: dqt kbm xsg
lpf: lhl sdb
gbl: rtb
ljm: zrr
htp: zts fts jsg
xzf: gcm
zhr: klp dmp vbv
dkm: dvp psb plv
pbg: xmp zkx ncz
ptc: fdh
lll: mdc qtk ssh gnb kcc
tdp: nsr vbv
bcd: mkl sht sxj nsb
zsr: flh rhp xbg
xcj: rfl zdj hfp dfm
zrg: khp czj shj xmg
dhq: xpc npr lpb
tgl: vkv zpv rdl rzb
pdm: zmj xqg bpz qkj vjp
rkv: lcz fdr rfn bfg hqf
pzq: ndl zjj ltn ggl rmf lpd
htb: mds
rqn: sjz bgr crr zqx
dgp: kbz cqc
mnb: rtb
dtp: mvc jfk ttv jck zzt
rsn: cnh djh hsb
ngm: nss qmn nks ccc
jcr: fdd vzm
qml: hzs mkq vkn
kqs: fxx
pbf: bln
dtk: gbn vtd vlx klc
fph: mlr pcj
gqk: fdd vxm
jmv: mmc ttt qbx trl
nfh: sxz
vbn: gqz nrk
kjm: hzs jvk kqs
dsk: tns
jfn: krp qrh pdd
mbr: gfq
xmx: vsv
svj: nvv ntq vxl gtc
qdc: ntv
dtf: qjf cbm mlf qlm ggl
fbh: tmt dqc vrf
szx: qzk chq
hxj: ldh rmc
rzs: mjz
kgc: blf dqc
rbz: zvm sbs
nrn: pbg mpc vks
nnz: bxk rmq bzl mxq
gmb: glb jfk bvj cpt
nnc: nhh
khp: cgn
tzq: tfp ffr
mnf: pjc hqs
vnr: pkh phl ccc vtd
pfp: qlt tzs
vsp: rjb zqn
xfm: fvn xfb tkj
vqt: rkz gpd
nrk: rkf
qvr: fvn
ccs: qms lhk bhz jzq
qnr: gbn bzk gfs
rrr: tmz rsl ckh
rqv: bgb ckl chk
pbq: xpf sxz qrm
jbj: mkm ths rbz
xqh: rmf prs
qmn: dlk jnq kpd
jbr: ckm kqb
zrp: jzx lck lzs mzv clm
rmq: hmt htp
mzr: psk dhg tpl xrr qrt nsb
lsx: rjb zqn
qrn: hsf vfj bxh smj knx
tsf: tvp tvm cmg vbn
tvg: hqx nlv tzq
txn: cbd ntr ztn hst
klc: vqz dlk lzf cfm tsn
brx: ctz
pxp: xzq nsq
brv: fvs lqf
rhs: qgx mpv tzt
cqm: plp gzn qbf tvt
tbf: fdh qvr ptr hpm mhk
qfk: sgf skp tjs rhp
qzx: clv tmt
fvs: hhv rtj
rpp: qbp klx sfb gnn
tjj: lcd
hkx: nkn kzz zfz
txf: dzq
vts: plm zts
xls: vkv zvn lpf jnq pkl
rss: lpf qvn lqj dhh
xgl: znl pxm dks
bzl: nhh
jlj: htl
hgz: hfg kcd qfd hgc
gqz: lhn npj
qfd: hqb
xcd: ddv rrs pzm qfn
csq: bsq rtr
xmh: nhc ncd dmp zjx
ffq: ggr xrp pcz
dsg: gql tvf
zvn: phl
lxv: bhz lcd hqx
xqd: rsv pbx mbr szj pvn
crb: zmn xjz
bzz: kkn fpc cjs znx bjh nhh
rqk: xpf frf tfh
jxq: kbm rqg gpr nrn gzx
bkg: srr rbb zfg cxf
mcd: jqp jbx lbf zkx
hgg: tvh rdl xsq fll hnv
chb: kbt kck vls hst
xpn: djh
btl: xsg nmk vjf pfp
pxm: bnl hqf brh
lmn: fcl lsx lxj ktv
jkp: sdb
pkl: kzz
jth: gvf gqk plk mkb rhs
dzk: lzp nnb pql xbg
pkh: dlk
scz: frx
qpp: krg xdn vdd
ffx: dgp bcx qst grn qfj
trn: nmq mzj mgd pbk
gzv: lsh vxr hfz
gzx: kmb qhz
bsj: vmv gvn ldh
rls: vfb ssh nbp
vcm: nnc tzt zqg hkr
zrk: khj nqr jqp zjq
rfn: gzh hfg
ccp: zmr xxx
vdt: smh
zvq: ksl fbj vzr
rdv: ljm ctz nsr kdq
qdq: zzl
jlk: nlm fqh xfb pzh
tpz: kdt hlz plq tvm
dgl: zjj
mqn: sht jqz jrs
bnl: dfg tck
zbp: xpc mvk hsf
fxp: mhs fhb lsx
glb: svj fcm mjd
pbx: trk plq plm
zqv: qvn qdp
mkp: mjb knl kvh dlv
zkj: svz dqt
zdj: zqn ccp bhz
kqf: kbt mpq rls drg
hbn: qpp nfb vjr
ghz: lfq krp ckc nmv
fzb: qtv kqs xjc fxr
hrg: cgn
zgv: zmq zlx zck
qtp: zkr tjj ltn lsf
kfk: jcl bcc lfx kkn
sfv: lvd xmz vjz bgt
jtn: hxj
nlv: mqh
ndg: gtc
krn: krp qrh
zjt: dvk pks zqv lhd
flh: bsf xpc
mpk: cjv njr kck
lzp: qsn jjt
qxq: dzp
grn: qdc vgs
tsn: rlh
jsn: bph sdb xgm ctq hqx
hsx: qvr fhf qqn
xjk: rbj
zxn: vjm thr mjd
kxz: rbp dfm dgr trq
lsf: rrd dbj mlr
frr: bqd mln fxl tgp
spv: pmh jrs rfk zlv rvc
qkt: ptl mzv
ctq: lhl trz bmf bts
ljk: gcp nqx
ncb: kpd lhm mcf
rqt: tnx dgc jzq thb
zdp: zvn kvt bsc
xrp: qdq cxf gpb
rrc: frx vmg
vdm: vbv xrs qrm qkp
mst: vnb mkl
fch: lpk rcg
fxn: qgx ptz gcm qfn
bbp: lcl
jzf: cck rvc
qng: dqf ghj zrp kth
dxr: bgd
ngj: jkp jjg cpm
hgl: rrt ksn slh jhz
nrm: xdj fts plm kfq
vgs: nmr pbf gqk bqm ths
xrj: jsc pvz fch jsz
fbn: tmf fxj nmq
jqc: njc
qmt: qnb fxx kcc vfb
xnf: rsq jbr gpb ksc
tvh: tjj
npj: gzh bcq
nmq: pkr
hkc: lln
tlq: npr thb knd
pfj: bpr jdr gtj kvh szl
vtp: thg jlj
vhz: znk qhm
txl: vjl
hxv: mnj vfm vvt tvj
zjq: bbp snn srr
ckc: vgp mpn
lzg: cfj klg
bpv: vsp cbx
cbj: fpv
mgk: lcl
sqg: kck tkj
lds: zgv nxg
sjf: qqn gzh
dmr: gff kdt dks nbp
jbf: phl
sgn: bcx dsr krg
nnb: pks
pzk: cgc bxk qst
tbs: vzb rpq
vqq: lgb dgg ncj vxm
lqf: zrq
xxf: kgv qjc vfm fff
kjb: krp qlm
vbv: ckt rfm
bbk: psj
bxk: drz
lzf: gdc kmb
ghv: rlh vhq ncn bqg
brh: ffz
cxf: dfn
xxb: kkq jsp fxx bch
drg: hhv
vgf: cbj ppt kqb
jfs: drz szx cvx
gcn: fbj mfh bpr gnl ttb
dtj: mlf zxn hgt vjp
fzp: knx dqv qdq
xtv: hlz hpk rrq
kbj: rtj
bjs: nmb tdl
kcc: cqz
jlf: klx krq mcf fbg crr vpl
fhx: jnf rrq rgv pvn
rxq: fcm jqc nmb cbm vgf
ffr: zfg jgc
lvf: thl ncj lzg jtv
ltv: xtm xtl dgl jnq hrj
gvp: npk lds rxm zxb cbv
tkr: jtv
hmx: qzp hph fhq
xjs: zbj fqh hvz
rxj: jjt xbg bsf fff
hhd: hsb ffq txl vvb
jkh: fgq
qsj: fnj mpk
vfn: llt trr
zxb: spk rqr
qts: qkp kth pxk kjh
czz: ncq zxb nzg
bnj: gnl srv cgc vfl
slt: zfz mkd dfj
dfn: vxl zpm qmh
rfp: sdm gzn xbg
kss: kjn dkh trk hht
gnl: clm nzq
ldd: lqf vpn fbh tvp pzm lxs
trz: npk
dtg: zck kzj
fgt: hrg
xmj: btc dkm jfk jln
djz: frx
vzb: ffz lnt
qzr: djz bkd jzf
bbh: qvn
xlz: zhr mmb mkb xcn
pgs: hsd xzf kgg
hnq: ljm kck
nch: zrq gbl krb
lxs: mjb szj rmc
mzp: dgr xlr dgv hsv qzr
npp: tvf ldt tqz txc scc
rfb: cck bsc vqh
fmd: jzq fpv
njr: nzq srt
brq: zqv jrs hls kpr
rdj: skx
kgr: grf tgn
clt: mzq bpr sgd
fcl: hnv
xrn: snr svz ggp
lsc: jtn pvd
jst: qhm
pmd: zgd mpk dfg
snr: bsc gbn
kgv: cqp rbk dgv
rbr: thb
dzg: bxh dzq xpc tsn
czl: jdp qjp pxd ptr
cdf: blk psg xqh
mkb: mgd
hdv: vjf ndg cnh
gsl: hvf cxv hmx fph qsn
qtk: mpq
fff: lhm lzv
vzr: ttt hpk
rlr: gjd szj dln
jck: vck jzz xdg
gcb: xrx tvv ksn
bmn: trz thr
hhh: pcz cpp lzp
ccf: hgc ltq mpq zgd kdd
bqv: pbd kjd zmt zvm
psv: tph prs tlf
zhm: djh zbt zrl vqh
rdd: vvb bsf qhl
rfk: gbn
sjz: blk rjb
kzc: hrg pks xmr
qst: gff
ppr: hrl vfb bpr
kbt: dvl nfl ztn
lrv: rxv hfp bgd nnr
nqr: zzt
knl: hrl xjs
qtv: nmr
cmr: scz djh rvq dcm
hmv: rtv njd vqv
ccc: tnn
vlx: bts qvn njc skp
qzp: cbj
hzs: xmv
lmh: ndg hnb
gvf: gcs xfb mdc blx
vtf: rxh gff gvn kvm
lzs: ptc kgc
pmh: mpc tjj trj
hhz: psv dhq nvk nnb
dhb: jvk lqv bvl nfl
lkc: djp cck
ksb: pvd gxx znk gvn
psh: xrr
lst: kdt blf trk cjs gxx hqg
kvd: hck btc
hrj: lqj
vjf: gcd
vfl: gcb chq htb
mkl: sqb dtg jbf
bkv: tvv fkp vpn
nlb: pbm zgd pzk znm
rzr: hgr bgn kgr pxk jnm
nmk: vsb cmz
ccr: srr psh
ctn: dtm mbq
jhg: brx rfn
vhs: rdj hhv lhn ptc
xkt: fqh fxf grq bpr
dbl: hhv
vlt: gjd
jjn: vpg krg mxq lgb
vkg: kmk sjk vfj
bcx: lhr tzt
mjd: tdg ppt jmg
gpb: pxp bgj
hfk: nfd brv nft gff
trk: jhg rjc
xtk: gqz qlb mkm
qjp: bcq
rjt: rrq mpq stl vgj
tvm: drz xtf
vfb: ckb
bnk: srt jqg gps
dhx: jzq szp fvk
xkm: cqz kmz
vjq: vmv ckl zrz
krq: srr
nzg: zrl ncn
zxh: znx kdd
pzm: kbj pbq
txm: dkp bbp hls qlt rsn
fdf: cbm gzn gjc hth
czj: gcd
gnb: zrq sgd
zlv: kqb ddl lhl
qll: spk gcp dhp
vzp: hht xvb
vcn: gbl
vrm: mcf rlf mvk mpn
bdn: flf jgc gcc hfp
rvt: vfn ncn zgr
jdb: mhk tnq nsr
xzs: zmr trr pkh
mqc: sfn pbm jhz
thl: zzn
fhq: rjb
cmg: zvm
mbq: jpk
zhf: plv xmp gcc bxg
gfq: sgn fqh mmb
vmv: fxx
vmc: mgk tlq ddl
vxr: kqg ccp
qgx: tck
blk: lzv
gjj: xzz
cnr: bts dbs gbn
xpm: qcm cqp
szv: rlm xtv znz lmf
rkr: bgb
vlj: nsq xpm dzn lhp
ltp: fpc mbq tmr rmq
nnr: nmp
vqk: psj xpf kcc hgr
fzj: vpl hlt jpq czj cth
lnt: gkr vbv
vlg: fxr sfb bxg
rhp: lbf smh
hvq: clt cxl zxh vzr
tvs: vcd
dnf: qbx frj vls bnk
vgp: nsq qdq gjj mkd
fpc: qhm
hqs: xqg
tfh: szl jnf
qgt: nct dft cgn
hfs: htl vxr hrg gkq vtp
thb: vkg
xrg: vzr zrz cgc
mcb: blx tdm xrg zvm tcl npj
rhd: nfm mhs tnn rcg ttx
hvl: rss rrd qvn xts
qph: vfq pbm nzq qkp
nfd: rjc ffz
nsb: fhq xrr
cpp: gnc vdv
zcp: trb fll ftg pll
llp: xbt tzq qdp
dhg: qhz cbv fbt
jxx: vsv qhh vhs kqf
ksp: gqb vjz vlt ncd
snt: gzg tph jss
kgg: frf
qrl: tds jlm dkx bdn
szp: npr pql
qhz: pcz mlr sjk
vrp: ftt htp pbm hnq
kdc: rdd smj
mhv: vlh qcm bvj qlt
pvm: llt dvk ggp dzq
ctr: nmp glf rbr jmg xxx
klv: vdt sxv rlh vtd
sns: qhm hqg znl
gxh: vpz qtv hfq
khj: djz fcl xxx
kkq: ckt
kvt: dfn
nlm: sql kdd ths
mnj: xpm qmh xts llx
vng: kbz gvn
gps: jvk
bth: hdv ksc hqs mst
xzz: xbj xbg vtd qgl
ldt: jdb zjc kbl ckl
jnt: tkr xmz
lkg: clv bkv qkt tqz
hth: jss
rzg: cqk qtk tdm
nqx: kpr tnx xzq
dfh: gcs kgc fqs mjm
nkc: bcq
tvv: qtv xxl nfk
hgr: hqb njs
djh: ltn
glt: txf ffc lkh rfp
plp: jbx vsb zfg
zpd: shc xdf kdc pkh fxp
bgl: pkr ztn qhh
ddr: cjv ftt kgc zvm
hdz: qrz qzr kqz zsj
rrg: vvt slt lcd sdb gtc hrg
nxc: zrl hqx xsg xbg xmg
tvj: nlv shq dvp
rjf: ztd ttt
mdb: hnb tsn bqg jln
xdg: zfz vxl
tfj: lxj pxp zln sqb jbb
fgq: kdq fkp
fvk: xpn ckx
srr: rdl
jjg: bpv nkn xsg
rrs: kth dkh
mfh: drz jdp
mzj: qvr zqg znl kdq
npf: qzd ckh
vrf: vhz
rlh: kzj lrs
gmv: ksl ssh brh xcn
jtz: zmp
qbp: vdt mhs qbf hpf
hpf: lcl
drh: xts ckx dqp
bzk: jbr kjp
chk: zxh krb bvl rjs
kfn: xmr zzl dgv
mpv: ljm txc
lfm: hph mpn hbr
slh: jvk rjc
gpr: bxx bgd gkq
bkt: mbh bxg
shh: pcj sht jck fxq
vcd: fbj lck gjt
dsq: nmk cpm rxv zkx
hck: sxj vqh
rpb: dck fld rsl
xts: jqp
dkx: hqs tnx
nzk: xkm vcm nvz fhf mhk sqg
fbg: qmh
vdv: kzj
zqg: xmx
zzk: ckx pkl ncz rsn
sfb: cpt
bqd: xvb
zmt: kdq bch
rbj: qjp
lhp: lfm nkk ggr fch
fxd: mrn bhz sfj cjp
gmz: fdr qsj zrr kfx
qkp: nfh bqm
pns: kqr xlr qkj
fbv: bkb gxd szf kfq
cvx: qrg
mhx: szx bvl dql jgt
rfl: krq cfm
tnx: jsf
plk: mmc jgt
tcv: qpz bmf lqj ckc rbk llq djg
cxv: ncn rsq
clp: jgc fbg
hvs: plm gjd
vlb: txt nkj llx hph
zrl: gcq
gcc: hsv qsn
cxl: kcd rhs zfj bjh qzd
qmh: qlt
jhz: gps vrf qtz
dgg: mdc
jbg: czz rbr gbn rbp
zvk: xrx tmz tbs ttb
kdd: hfq
gkr: qzd qlb pxh sfn
jbx: pxp lpb
krz: gkz njc dbj
dvc: gtc txf prg flh
cqk: cqc
crx: zvm pbf tkj fjg
mrg: xxd psk sdb
hgt: prs
xjz: lhr
knx: sqb
fbj: zrr dck fdd
kmz: pbf vmv fxf
kvz: szl ztd
png: spf xzf jfs hsd
mvk: bsf
nfl: gzh
czh: bln slh rjs mhr
lvk: hnv kbm
ddj: txc gjt lln dqc hpk
dhl: kzz vgp fmd dvp cbv
dqf: lgb rtr mds
lpd: kmk hdg
grf: zjx nms lht mdc
pzv: lst kjd lsc qqn
fms: qbf kqp gnn lxj
ckn: dhb rtb csq
tcl: jlt cnm cgc
gjz: gdc jzq kqz
pbm: lbm zmn
nkn: mbv
tgn: gps npf
gzn: crr
xxd: frx hrj
ntq: rdd dxr rrc
hkh: qdc xtf hqf xqm
bkc: hmv cbd vgc frj
dlr: hbn gcn ckb drt
lrr: hpm npf qrg fdp
qqf: gtx dql bln qsj
vqv: tdp dfg lgx vjz gdd
csb: rmc rrr jqx dln
snh: lhn cpz
slm: hrj dvk flf
hvn: lln dfg ndk brv
snn: gcp nlv
fdr: kgg vng
vjr: rbj rlm kmz
qms: rhp zlx
kqp: rzb gjc jkp psh
bgn: qml nps clm
mrr: bgr vhq thr
fcb: lxr jfn pkh qpz
klp: fhf sbs jtn
qvm: ldd mnb htc ctn
bmv: mkm rsv hvn
qzk: qdc pgz
hrl: dzp rfn
zmj: bbh qdp blk
gkq: kjb szp
gtx: qzx mnb cvx
vdd: zjc xfb tkj
zrz: njr mmc lht
hhv: qxq
ndk: cqk mjb bvl
cfm: klx
rbb: ckm krq nlv
fhv: jtv ksl ltx
dvp: gxb
tjb: rbb flg zmr fpv
mcf: jgc
fcr: bhz mhs vfn bkd
gzj: znz kgr nzq
mrn: pdd gcd
rlf: bkt qgl
nxg: jjt hdg
lqv: kkq xtf
mth: kff qqm hmd krg
fxf: drb
dsr: ftt rfn
kpr: tqn jqz
npv: jrs tfp dhg gzv
bkb: lzg tbf
dqv: gtc
qrr: lhn hgc lsc xmz
snl: qhm
ckb: rjs rtr
xxc: jkh pgz dsr
qzh: kgg zmp rgv
shq: nmb
vds: xsg txs ncb nzc
cpz: clm gvf
llx: ngj
stl: shv jst jdp nps
gcp: cnh
xbj: jln jgc
cjr: bmv gjt zbj ffx
mps: nss ktv nct rvt fxr
zbx: zkj zpv vqz
znj: xzs txl gpz hqs
dnl: lpb pks prj khp kvg zgv
dft: gdc sjk
vxl: kbm
lsl: rbp hgt hpf lsh djg
kmb: hls
klx: trb
vfm: qsn npr rns
lgx: gjt nrk jsg
tkj: bsq
xmg: fxq
szf: fld
rkf: srt
bcq: szl
prb: knl xxb qgx dlv
lvr: smh jsf rzs ggl
txs: bgr vvb
grd: dfj kzj bjs nkn
lql: vrs
mvp: hzs sns tck mpv fnj
dvn: nnr shj jqc dqt nmv
vck: pjc zsr pkl vtp
ddc: nfh tvs slh krg fpc
nmv: thl tqn sht
fqx: jqp vmg
fzl: rcg gcq cth vtp
fjg: rkr rsl kkn
tgp: xtv zvv fqs cqc
rxh: zvm
jtq: pxz pjk dhp vmg
nvk: zdp vtp lrs
bft: fvn tmg lqf jbj dmp ctz
hpn: ghj nmr kcd csb vlt dsk htb srv pxm
rfm: xql gcm
xrr: dfm
vgv: ctz
znx: kvh txc
gtj: zgd
hsf: dkx jjt
cqp: rmf
ffz: mzq
cdb: hsx drg pbd
zrx: prg rgp mrg jln pll
rzn: mnb xfz vjr fsl kjh fkm
qrj: hsm ttv cqr zzt
mvc: qkf ljk xqh
vvb: vjf
tmf: vgv qfd clm
nxj: jst vjs hzs hhv
kbg: lrs tnx hnv qgt pns
kqr: vgf shq gkz
gxx: fld mln
jqg: zrq xmv qxq vpz
ftg: shj rcg
sgp: vzb tvf jlt
lkz: dkh chq rjf
vmq: xfb srt gxx kck
nms: vjz hfq vpg
ggr: thg tvt zkj
bxx: bkk xxx fqx
njd: pbd
dcs: qhz glb bmf hls
rpl: nxd rbr vdv cck hnb
pkz: vtp rhd zbp hth xdg
ttx: bvj lzv
zrd: djp tlf mqh
kjp: mbv
vxm: bhq
ltq: mln nnc pbk
ktl: bhq tmz dbl qrg njd
blx: zbj
prj: bts xxx
sxv: bzk nmb rbp vfj
hkr: xxc bxz mgd
vzm: gcs
bxh: hfz sdm
sxg: crr khp zqx vsp
bfg: ckt xrs
rng: cnr lnn lzh vnr
chq: rkf
rvq: bkd gdc
qhr: mlf gxb vsb vkv vqt
mzv: qxq
dnq: xpn nmp thb qjf
mjz: jnq
zkr: zzm fpv vsb
ljf: jpk qkt gbl fqs
qpv: ppr hxj zzn vjs jrh
mkq: dxx sjf bgl svs
qkf: gjz vsb vvt
sfm: vjl dbs lrs czz
jzm: jrh zmn mbq scc
nmg: nnz xjz dln lht
tdl: svz
dzq: thr zzl
vpl: bkk
psj: mzq qtf
rgl: fbn kff qbx shv
bpz: sgf vjf
xqm: ptb gql
zln: jsf tvt bvj
krp: rcg vdv
jqv: crb ldh
djp: dzq vqz gfs
vxh: jvt dck vbn vhz
rzb: ddl
nzc: cqp rzb
lck: znk kbz
qnb: ntv ftt
xvv: lhd txt hhd ncn
hph: dgl jpq jzq gpd
lrd: ckn pbk qtf cgc
ckz: sjf dtm
rrd: hhh rxv
lht: cvx szj
gvn: dck
vgj: hsd jtv nfh vrf
lcz: qtz vjr
ckh: frf
hqg: mpv mmb zts mln
dpb: xtl vjl ttj
ptl: tck lqv jlt vcd
qkm: fmd xmj kmb lvk
jsc: pdd spv vlh
lhk: lzp dvk
mpc: tzs
cbd: qtf ddj
bcc: fvn
hlt: txl tsn bjs
dxn: jcl fgq cnm khz
kmv: lhm bxn jss lfq
fpb: drb dcx zbj fts
mxq: fvs kgc
vjs: rbj zgp mzq rxl
sbx: str cjv cqk gtx kbl
lvm: rrp nnb qqp flf
djc: xdn qqb xcn
lbm: dln
dcl: krb zmp znk qfd vng
llf: vcn rtj njr
hht: qzh vcn
mfk: hkc qqn gtj
tdg: mkd tdl
tgj: dft dxr djg shq
xgm: tfp dfn ddl
kfq: mkm
hbr: gcq xpn nmb
tqp: hpm jkv bgb
vks: hnk jlj lxv
mhl: htl sxj pll txl
pgz: xdj
dvm: lsx vvt nmp
hdg: cmz
fbx: vkv hsb dkx qrz
mhk: qrm cmg khz
fbb: smj lfq psv tvh
cqg: xqm lmf gdd
zpm: sjk
xmz: lhr
hss: bbs mvk kvt kmv
rgp: snr
plv: mjz ttj
lmf: qkp xkm
ltt: dgr djz bbh vpl
ddv: lck cfj
dsf: lnt kvm vfq
jtg: fsl xdj ttb kvz kbj vfq
rsq: bgr hsm ggl
tlf: tqn sfb
sdk: rdb cqz xql lgb jvk
tvt: kzc ccr
zsj: lvk nkj cnh
lfq: cfm shq qrz rfl
ttv: qzp rns
tmt: dzp
hdq: dhh lhl dqt prs
bgt: rdb klg ttt
ptz: ncd vsv ths
sfn: grq
rbk: dht lqj
jzz: sht zgr nxg
qxp: qrj mhs flh sgf
mjc: rxh kvz xkm qrg
qkl: bvl thl ctn
lph: ptr bjh rdb mds qfj tvf
tmr: bhv kcd tdm qhh
gcd: llt
bxn: bkk trj
ktg: hlz tns gnb
zdz: dck hpm rbg ckz dgg
mjm: ncj nfd mkt
gxk: shj crr kcz bmn
drt: rqv kdt
trr: qsr vsb
frj: vjz jzx dmp
qrx: qnr lzf mlr zbx fmx
pzh: hgc qhh
vpg: ksb fzb
vgk: kcz xqg krn mbq
cqr: rrc cxb kmk nss
zzm: vfm spk rdl lcd
jnm: hkc vjq xvb
stf: vxm ckz hnq tcx qrm
qqm: snl dsg zjc nkc
fcm: vkg nmv
xtm: bxn tqn
gpd: vqj dbs
gpz: btc shc bbp
tlv: rlf gzx txf vhq kmk gpd
ckl: htb mzv
mnl: vrs ntr jdp jvt
cgn: bsc
zkb: btc kqz vqj nnb
sgl: jtz lzs hvz snh
ktr: qqp dtg dpb sjl
gst: txs hsv
xvb: nfl gcs
bmj: npk gtc gfs fzj
vsv: zfj nmq
gmh: njd sfn ffz zjc hvs
kpd: trq
rcb: xbg dqv zfg
hfl: vdv cdf pdd tkn
bdq: hxj fkp ssh hst
ccm: qpz bgj pbg hnb tkn
xmr: hdg mqh
clv: lql
ffc: cbx mnh
vjp: tdg gst
kfx: fxl rkf ptc
nps: dsf sgp
tmg: rfm bfg gql
kdt: cqk dks
gcm: pbd
pxk: qrm
ztd: dmp hlz
czr: fnj xmx bsj hkc
qxz: hnk vqt xtm mnh
xtl: ggp rns
mkd: zpm rns
lgr: gcm jsp vts kbz
zzf: dxx tkr trn tvs pbk gzj
shc: lpk kvt
ssv: fgt gcp ktv
zgn: sgd dsk dxx dbl
zjx: tfh pxk
xfz: qjp mmc bzl
rjs: kgg
dbq: bqg zhf sjl dvm
cth: skp ppt gnc
gnc: svz
zgp: hqb lql xpf
psk: vqz scz
tpl: zzl zgr jfk
ghj: kbj lkz
lfx: kkq fdd rhb
pcz: cbx
qcm: llq
hnk: vfj
dql: vts qjp
spf: znk
rqg: rhp ffc rxv
mff: rtv kbl xxb
skx: frf xtf tmt
jcl: qzk dsk jgt hst rjf
lnn: xbt rbk ndg szp
zqn: llt qgl
cjg: sgl kff hvs cdb
zbt: hsm rjb
nsr: xjk hqf blx
pvz: rns krn hnk
xsq: tzs xzq qms
vlh: cdf
dgc: lhm hvf
nfb: snl vcs
pvn: plk pvd nkc
tds: tfp mht mnf llq sgf
cpm: ltn qzp
fxq: czj cbm cpp bns
fsl: dgg txc fqs
hbb: skp nnr qhl kqg
rrt: kbj znl
tkn: pql mbh
jnv: vmg lpk zvn
jkx: vqh dgl jnq zmr
nks: flf dlk bbh
rdb: rjc
zgd: cqz npf
sjq: snn rfl pts vlx
rqr: sdm mlf dfj
hgc: sbs
rrp: dht ckm qdp
qqb: kvh lhn npf
xlr: mpc lpd
lzh: jbf vlx
dqp: xxx hvf xmp
jfj: lkc bns zrd ckm dbj
tvf: dqc
znz: tnq htb
pvd: bln
xng: rxh bqd xtk xmv
jlm: qgl vck nzg
fpq: chf kqg drh vbc
cmf: zsj mht xmg hck fph
jsz: krz vdt nqr
vdn: fqx vdv
mlc: nnc kvh svs
dfg: kvm
xhk: vqk vzm bhq czl
rsv: mmc zmn
shv: xmz nft bgb
znm: ksn vzp khz qnb rpb bhv
smj: bkk
fll: rzs prj
trq: hfp
nvv: psg xxd
tqj: zgr ttx nkk vbc
dvl: bcq
cgj: fnj qfn bbk trk
dfm: mbv
phn: dqc svs ntv hgz
dxx: tns
qkj: rfb
bqh: lxv dhx dbj bvj
hvf: zmr
rql: mtp kjb kvd npk zhf
qfj: mdc svs
psg: pdd
mdt: fxl jcr pzh vgv hqf
lhd: rfk thg
hzx: nkj nmv vdn hhd
kgm: fpc srv zvq
cgp: fxr fbt knx vmc
zck: kqz qrz
gfs: bgj
zvv: dqc kkn tcx xzf zts"""

TEST_INPUT = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


def solve(input_: str) -> int:
    elements = {}
    for line in input_.splitlines():
        node, connections = line.split(':')
        elements[node] = connections.split()
    graph = nx.Graph(elements)
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    a, b = nx.connected_components(graph)
    return len(a) * len(b)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(54, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
