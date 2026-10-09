# Florida Amendment 3 Homestead Database, 67 Counties (2026)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23226000.svg)](https://doi.org/10.5281/zenodo.23226000)

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
| `data/official_losses_by_county.csv` | The state's official estimate of local non-school property tax lost in each county, fiscal years 2026-27 to 2030-31 and the recurring loss, in millions of dollars (shown as negative numbers) |
| `data/official_losses_by_authority.csv` | The same estimate for each of 548 taxing authorities (each county commission, each city, and each county's independent special districts combined), fiscal years 2026-27 to 2031-32, in dollars |
| `data/sources/edr-rec-hjr1f-impact-2026-07-10.pdf` | The Revenue Estimating Conference impact statement the two official tables are transcribed from |
| `tools/amendment3_impact.py` | The model, run against the Department of Revenue's 2026 preliminary NAL roll files and the 2025 Data Book millage table |

## The official estimate of what local governments lose

The two `official_losses_*` files are transcribed from the Revenue Estimating Conference's impact statement for CS/HJR 1F, adopted July 10, 2026 (Florida Legislature, Office of Economic and Demographic Research). They are the state's figures, not ours. They cover both parts of the amendment that can be measured: the larger homestead exemption and the cut in the non-homestead assessment cap from 10% to 5%. The conference did not publish the two parts separately.

The state's model differs from ours in four ways. It projects values forward with the state's own growth forecasts, it applies each parcel's actual combined millage, it keeps each parcel's other exemptions (senior, veteran, disability), and it reduces the homestead loss for people who move to Florida after December 31, 2026. Statewide, the counties sum to $8,714.4 million for fiscal year 2028-29 against the conference's $8,714.5 million total, and the authority table matches the conference totals exactly for every year.

## How our figures compare with the state's, Manatee County

| Piece | Our parcel model | State estimate |
|---|---|---|
| Homestead exemption, 2027 ($150,000) | $79.3 million | |
| 10% to 5% cap, 2027 | $2.4 million to $9.2 million, depending on market growth of 0% to 7% | |
| **Total, fiscal year 2027-28** | **about $82 million to $89 million** | **$85.7 million** |
| Homestead exemption, 2028 ($250,000) | $140.2 million | |
| 10% to 5% cap, 2028 | $3.2 million to $19.3 million, at 0% to 7% growth | |
| **Total, fiscal year 2028-29** | **about $143 million to $160 million** | **$159.3 million** |

Our homestead figures here keep each parcel's other exemptions, as the state does, which lowers the 2028 homestead piece from $144.8 million to $140.2 million (13,417 Manatee homesteads already have other exemptions that use up part of the new one). The cap piece depends almost entirely on how fast market values rise: a parcel whose assessed value already equals its market value is not affected unless the market rises more than 5% in a year. The two models agree within a few percent once the cap is included, and the remaining difference is the state's forecast of value growth.

## Sources

- Florida Department of Revenue, Property Tax Oversight, 2026 preliminary Name-Address-Legal (NAL) roll files for all 67 counties.
- Florida Department of Revenue, 2025 Data Book, `millage_taxes_levied.xlsx`: <https://floridarevenue.com/property/dataportal/Documents/PTO%20Data%20Portal/Databook%20Historical%20Data/2025DataBookFiles/millage_taxes_levied.xlsx>
- Revenue Estimating Conference, CS/HJR 1F impact statement, July 10, 2026: <https://edr.state.fl.us/Content/conferences/revenueimpact/archives/2026F/_pdf/page682-699.pdf>
- Ballot text, Florida Division of Elections: <https://constitutionalinitiatives.dos.fl.gov/Home/InitDetail?account=10&seqnum=110>

## How to cite

Klagge, Kevin D. (2026). *Florida Amendment 3 Homestead Database, 67 Counties (2026)*. Klagge Law, PLLC (StepUp Law). https://doi.org/10.5281/zenodo.23226000

## License

Creative Commons Attribution 4.0 International (CC BY 4.0). These are estimates, not tax advice.
