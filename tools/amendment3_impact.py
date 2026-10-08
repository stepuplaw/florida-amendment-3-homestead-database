"""Amendment 3 (2026 ballot, HJR 1F) county impact from the 2026 DOR NAL roll (added 2026-09-27).

For every homestead parcel (JV_HMSTD > 0) the model compares the non-school homestead exemption now
with the amendment's, on the parcel's 2026 homestead assessed value (AV_HMSTD):
  now (2026 figures):  $25,000 + the second exemption on value between $50,000 and $76,411 ($26,411)
  2027 (amendment):    up to $150,000 of assessed value
  2028 (amendment):    up to $250,000 of assessed value (before inflation indexing)
added exemption x county non-school millage / 1000 = estimated non-school tax saved a year.
Non-school millage = DOR 2025 Total Millage Rate minus School Board Operating and School Board Debt
Service (millage_taxes_levied.xlsx, current Data Book). Assessed values are held at 2026; the model
ignores other exemptions (senior, veteran, disability, widow), so owners who already pay little
non-school tax save less than shown. People who become Florida residents after December 31, 2026 are
not modeled (they keep today's exemption until their fifth year of exemption).
Writes data/amendment3_by_county_2026.csv. Estimates, labeled as such everywhere they are used.
"""
import csv, glob, io, os, re, zipfile
import openpyxl

ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "data", "sources", "nal_2026", "raw")
OUT = os.path.join(ROOT, "data", "amendment3_by_county_2026.csv")
SECOND = 26_411


def num(s):
    s = (s or "").strip()
    return int(float(s)) if s else 0


def pct(v, q):
    if not v: return ""
    k = (len(v) - 1) * q; lo, hi = int(k), min(int(k) + 1, len(v) - 1)
    return round(v[lo] + (v[hi] - v[lo]) * (k - lo))


def now_ex(av): return min(av, 25_000) + min(max(av - 50_000, 0), SECOND)


def millage():
    wb = openpyxl.load_workbook(os.path.join(ROOT, "data", "sources", "databook_current", "millage_taxes_levied.xlsx"), read_only=True, data_only=True)
    rows = list(wb["Millage Rates"].iter_rows(values_only=True))
    hi = next(i for i, r in enumerate(rows) if r and r[0] == "County")
    head = [str(c or "").strip() for c in rows[hi]]
    so, sd = head.index("School Board Operating"), head.index("School Board Debt Service")
    tot = max(i for i, h in enumerate(head) if h.lower().startswith("total"))
    out = {}
    for r in rows[hi + 1:]:
        if not r or not r[0] or not isinstance(r[tot], (int, float)): continue
        c = re.sub(r"\d+$", "", str(r[0]).strip()); c = {"Dade": "Miami-Dade"}.get(c, c)
        out[c] = (float(r[tot]), float(r[tot]) - float(r[so] or 0) - float(r[sd] or 0))
    return out, head[tot]


MILL, TOTCOL = millage()
COLS = ["county", "homestead_parcels", "median_assessed_value", "total_millage_2025", "nonschool_millage_2025",
        "median_added_exemption_2027", "median_tax_saved_2027", "median_added_exemption_2028", "median_tax_saved_2028",
        "p25_tax_saved_2028", "p75_tax_saved_2028", "share_no_nonschool_tax_2028", "total_added_exemption_2028",
        "est_nonschool_tax_reduction_2028"]
rows = []
for p in sorted(glob.glob(os.path.join(RAW, "*.zip"))):
    fn = os.path.basename(p)
    county = re.sub(r"\s+\d+$", "", re.sub(r"\s+(Preliminary|Final) NAL 2026\.zip$", "", fn)).strip()
    county = {"Dade": "Miami-Dade"}.get(county, county)
    tm, nm = MILL[county]
    z = zipfile.ZipFile(p); name = [n for n in z.namelist() if n.lower().endswith((".csv", ".txt"))][0]
    av = []
    with z.open(name) as fh:
        rd = csv.DictReader(io.TextIOWrapper(fh, encoding="latin-1", newline="")); rd.fieldnames = [f.strip() for f in rd.fieldnames]
        for r in rd:
            if num(r["JV_HMSTD"]) > 0: av.append(num(r["AV_HMSTD"]))
    av.sort()
    a27 = sorted(min(a, 150_000) - now_ex(a) for a in av); a28 = sorted(min(a, 250_000) - now_ex(a) for a in av)
    s28 = [x * nm / 1000 for x in a28]
    rows.append(dict(county=county, homestead_parcels=len(av), median_assessed_value=pct(av, .5), total_millage_2025=tm,
                     nonschool_millage_2025=round(nm, 4), median_added_exemption_2027=pct(a27, .5),
                     median_tax_saved_2027=round(pct(a27, .5) * nm / 1000), median_added_exemption_2028=pct(a28, .5),
                     median_tax_saved_2028=round(pct(a28, .5) * nm / 1000), p25_tax_saved_2028=round(pct(s28, .25)),
                     p75_tax_saved_2028=round(pct(s28, .75)), share_no_nonschool_tax_2028=round(sum(1 for a in av if a <= 250_000) / len(av), 4),
                     total_added_exemption_2028=sum(a28), est_nonschool_tax_reduction_2028=round(sum(a28) * nm / 1000)))
    print(county, len(av), rows[-1]["median_tax_saved_2028"], flush=True)
rows.sort(key=lambda r: r["county"])
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, COLS); w.writeheader(); w.writerows(rows)
print("millage total column:", TOTCOL)
