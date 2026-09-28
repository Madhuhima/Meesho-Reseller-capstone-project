# Narrative Report

## May — Ethnic Wear

**Context:** This update measures Ethnic Wear revenue for May compared with April.

**Insight (fact):** Ethnic Wear revenue increased by **77.1%** from April to May.

**Implication (hypothesis):** A possible contributor is the higher May category mix; as a next step, compare May Ethnic Wear order volume and reseller-level contribution with April before deciding whether the increase reflects broad-based demand or concentration in a smaller set of resellers.

## June — Ethnic Wear

**Context:** This update measures Ethnic Wear revenue for June compared with May.

**Insight (fact):** Ethnic Wear revenue decreased by **-58.74%** from May to June.

**Implication (hypothesis):** A possible contributor is the change in category mix; as a next step, compare June Ethnic Wear order volume and reseller-level contribution with May to determine whether the decline was broad-based or concentrated.

## Top-reseller narrative with masking

The five qualifying top resellers are referenced only by region and coded alias:
- West — ALIAS-19: INR 75295.09 total spend.
- West — ALIAS-22: INR 73882.33 total spend.
- South — ALIAS-12: INR 69936.46 total spend.
- North — ALIAS-06: INR 64238.97 total spend.
- North — ALIAS-05: INR 61825.02 total spend.

The `assert_no_raw_names_leak` check should return `True` for this text and `False` if `"Mumbai Reseller 1"` is inserted verbatim.

## Refinement self-score

- **Specificity:** Pass — the category, months, and exact percentages are stated.
- **Audience fit:** Pass — the language is directed to a regional manager and emphasizes an actionable business check.
- **Completeness:** Pass — each narrative contains context, a factual insight, and an implication.
- **Actionability:** Pass — each implication names the next comparison to perform rather than using a vague “look into it”.

## Chart-choice justification

### 1. Which month had the highest total revenue?
Use a **bar chart** because this is a univariate comparison of one measure (monthly revenue) across a categorical month field. The three bars make the month-to-month comparison clear within 10 seconds; the y-axis should start at zero and no 3D effect is needed.

### 2. What percentage share does Ethnic Wear represent of April's total revenue?
Use a **bar chart** for the category share, with Ethnic Wear's share shown against the April total. This is a simple one-category proportion and can be communicated clearly without a multi-series legend; the supplied value is **24.92%**.

### 3. How do the four regions compare on total revenue?
Use a **bar chart** because this is a univariate comparison of total revenue across four categorical regions. Starting the y-axis at zero keeps the magnitude comparison honest, and a legend is unnecessary because there is only one series.
