# Part 1 SQL outputs

`zero_order_count_demo.csv` deliberately reports `COUNT(*) = 1` and `COUNT(order_id) = 0` for RS024. A `LEFT JOIN` preserves the unmatched reseller as one row whose order-side columns are NULL, so `COUNT(*)` counts that preserved row. `COUNT(order_id)` ignores the NULL and correctly reports zero matching orders.
