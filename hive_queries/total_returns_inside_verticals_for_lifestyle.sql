SELECT product_categorization_dim.analytic_vertical AS vertical,
COALESCE(SUM(rvp_fact.return_item_quantity), 0) AS returned_qty
FROM bigfoot_external_neo.sp_product__product_categorization_hive_dim product_categorization_dim 
INNER JOIN bigfoot_external_neo.scp_rrr__return_l2_id_level_hive_ss_fact rvp_fact ON rvp_fact.returned_product_id_key = product_categorization_dim.product_categorization_hive_dim_key
WHERE  product_categorization_dim.analytic_business_unit IN ('LifeStyle')
GROUP BY product_categorization_dim.analytic_vertical
ORDER BY returned_qty;