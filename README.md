# Florida Amendment 3 Homestead Database, 67 Counties (2026)

What Florida's Amendment 3 (November 3, 2026 ballot, HJR 1F) would save homestead owners in each of the state's 67 counties. For every homestead parcel on the Florida Department of Revenue's 2026 preliminary tax roll, 5,251,737 in all, the model compares today's non-school homestead exemption with the amendment's $150,000 exemption in 2027 and $250,000 exemption in 2028, and multiplies the difference by the county's 2025 non-school millage. The table reports the median homestead's assessed value and estimated saving, the 25th and 75th percentile savings, the share of homesteads that would owe no non-school property tax in 2028, and the county-wide reduction.

Compiled by [Kevin D. Klagge, Esq.](https://stepuplaw.com/about), a Florida estate planning attorney (Klagge Law, PLLC), ORCID [0009-0002-1385-8498](https://orcid.org/0009-0002-1385-8498). Modeled on September 27, 2026.

- Canonical page with the county table, a calculator, the ballot text and the citation: <https://stepuplaw.com/florida-amendment-3/>
- Source repository: <https://github.com/stepuplaw/florida-amendment-3-homestead-database>

## What the data shows

| Measure | Figure |
|---|---|
| Homestead parcels modeled | 5,251,737 |
| Estimated statewide non-school homestead tax reduction, 2028, at 2025 millage | $7,595,622,879 |
| Largest median saving a year from 2028 | Broward, $2,604 |
| Smallest median saving a year from 2028 | Liberty, $245 |

School taxes do not change under the amendment. The school portion of the homestead exemption stays at $25,000.

## Method

For each homestead parcel (homestead just value above zero), using the parcel's 2026 homestead assessed value:

- Today's non-school exemption is $25,000 plus the second exemption on value between $50,000 and $76,411.
- The amendment's non-school exemption is up to $150,000 of assessed value in 2027 and up to $250,000 in 2028, before inflation indexing.
- The added exemption times the county's 2025 non-school millage, divided by 1,000, is the estimated non-school tax saved in a year.
- Non-school millage is the Department of Revenue's 2025 Total Millage Rate minus School Board Operating and School Board Debt Service.

**Limits.** Assessed values are held at their 2026 level. Senior, veteran, disability and widow exemptions are ignored, so owners who already pay little non-school tax save less than shown. The millage is a county average; a parcel's city and district rates may be higher or lower. Counties and cities may change their millage. People who become Florida residents after December 31, 2026 are not modeled; under the amendment they keep today's exemption until the fifth year of exemption.

## Files

| Path | Contents |
|---|---|
| `data/counties.csv` | One row per county (67 rows) |
| `data/counties.json` | The same rows as a JSON array |
| `data/schema.json` | Data dictionary (Frictionless Table Schema) |
| `tools/amendment3_impact.py` | The model, run against the Department of Revenue's 2026 preliminary NAL roll files and the 2025 Data Book millage table |

## Sources

- Florida Department of Revenue, Property Tax Oversight, 2026 preliminary Name-Address-Legal (NAL) roll files for all 67 counties.
- Florida Department of Revenue, 2025 Data Book, `millage_taxes_levied.xlsx`: <https://floridarevenue.com/property/dataportal/Documents/PTO%20Data%20Portal/Databook%20Historical%20Data/2025DataBookFiles/millage_taxes_levied.xlsx>
- Ballot text, Florida Division of Elections: <https://constitutionalinitiatives.dos.fl.gov/Home/InitDetail?account=10&seqnum=110>

## How to cite

Klagge, Kevin D. (2026). *Florida Amendment 3 Homestead Database, 67 Counties (2026)*. Klagge Law, PLLC (StepUp Law). <https://stepuplaw.com/florida-amendment-3/>

## License

Creative Commons Attribution 4.0 International (CC BY 4.0). These are estimates, not tax advice.
