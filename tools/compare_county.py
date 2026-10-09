"""Compare our parcel model with the state estimate for one county (added 2026-10-09).
Usage: python3 tools/compare_county.py Manatee 8.2484   (county name as in the NAL file name, county 2025 non-school millage)
Homestead piece keeps each parcel's other exemptions (added exemption is limited to the parcel's non-school taxable value).
Cap piece: non-homestead, non-agricultural taxable parcels; assessed value grows by min(market, 10%) today and min(market, 5%) under the amendment, at an assumed annual market growth.
Expects the 2026 preliminary NAL zip files under NAL_DIR (see README Sources)."""
import zipfile,glob,io,csv,sys,os
NAL_DIR=os.environ.get("NAL_DIR","data/sources/nal_2026/raw")
county=sys.argv[1]; NM=float(sys.argv[2])  # county non-school millage 2025
p=[x for x in glob.glob(os.path.join(NAL_DIR,'*.zip')) if county in x][0]
z=zipfile.ZipFile(p); n=[x for x in z.namelist() if x.lower().endswith(('.csv','.txt'))][0]
rd=csv.DictReader(io.TextIOWrapper(z.open(n),encoding='latin-1')); rd.fieldnames=[f.strip() for f in rd.fieldnames]
num=lambda s:int(float(s)) if (s or '').strip() else 0
SECOND=26_411
def now_ex(av): return min(av,25_000)+min(max(av-50_000,0),SECOND)
hs27=hs28=hs28_naive=0; hcount=0; capped_by_tv=0
nh=[]; ag=0
for r in rd:
    jv=num(r['JV']); av=num(r['AV_NSD']); tv=num(r['TV_NSD']); uc=(r['DOR_UC'] or '').strip()
    if num(r['JV_HMSTD'])>0:
        hcount+=1; ah=num(r['AV_HMSTD'])
        for lim,acc in ((150_000,'27'),(250_000,'28')):
            add=max(0,min(ah,lim)-now_ex(ah))
            if acc=='28': hs28_naive+=add
            # cannot remove more taxable value than the parcel has (other exemptions already applied)
            addc=min(add,tv)
            if acc=='27': hs27+=addc
            else:
                hs28+=addc
                if addc<add: capped_by_tv+=1
    else:
        try: u=int(uc)
        except: u=-1
        if 50<=u<=69: ag+=1; continue  # agricultural
        if tv<=0 or jv<=0: continue        # fully exempt or no value
        nh.append((jv,av,tv))
def cap(g):
    d27=d28=0
    for jv,av,tv in nh:
        j27=jv*(1+g); j28=j27*(1+g)
        b27=min(j27,av*1.10); n27=min(j27,av*1.05)
        b28=min(j28,b27*1.10); n28=min(j28,n27*1.05)
        d27+=max(0,b27-n27); d28+=max(0,b28-n28)
    return d27,d28
m=NM/1000
print(f"{county}: homesteads {hcount:,}, non-homestead taxable non-ag parcels {len(nh):,}, ag skipped {ag:,}")
print(f"homestead 2027 ($150k), floored at each parcel's taxable value: ${hs27*m/1e6:,.1f}M")
print(f"homestead 2028 ($250k), floored at taxable value:              ${hs28*m/1e6:,.1f}M  (no floor: ${hs28_naive*m/1e6:,.1f}M; {capped_by_tv:,} parcels limited by other exemptions)")
for g in (0.0,0.03,0.05,0.07):
    a,b=cap(g); print(f"cap 10%->5%, market growth {g:.0%}/yr: 2027 ${a*m/1e6:,.1f}M   2028 ${b*m/1e6:,.1f}M")
