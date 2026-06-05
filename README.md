# Beverage Vendor Analysis
Built an end-to-end analytics solution using Python, SQL Server, and Power BI to identify supplier concentration risks, optimize inventory management, and improve procurement profitability.

---
## 1. Background and Overview

### Business Context

Premier Beverages operates in the alcoholic beverage distribution industry, managing a complex supply chain that involves multiple vendors, diverse brand portfolios, and significant inventory holdings. The company purchases products from various suppliers and distributes them through retail channels, requiring careful management of procurement costs, pricing strategies, and inventory turnover.

The analysis examines operational data spanning purchasing transactions, sales performance, gross profit generation, and inventory metrics. Key operational processes evaluated include vendor procurement, inventory management, pricing effectiveness, and stock turnover efficiency.

### Business Objectives

The analytical engagement addressed four core business objectives:

1. **Optimize vendor diversification** to reduce supply chain concentration risk
2. **Improve inventory efficiency** by identifying slow-moving stock and capital tied up in unsold products
3. **Enhance profitability** through data-driven pricing and promotional strategies
4. **Evaluate vendor performance** to distinguish between high-volume and high-margin supplier relationships

### Key Business Questions

The analysis answered the following strategic questions:

| Question | Business Relevance |
|----------|---------------------|
| Which brands have low sales volume but high profit margins, making them candidates for promotional pricing adjustments? | Identifies opportunities to increase revenue without sacrificing profitability |
| How concentrated is vendor purchasing, and what risks does this concentration present? | Assesses supply chain vulnerability and diversification needs |
| Does bulk purchasing generate meaningful cost savings? | Validates procurement volume strategies |
| Which vendors contribute to slow-moving inventory and tied-up working capital? | Targets inventory optimization efforts |
| What profitability differences exist between top-performing and low-performing vendors? | Guides vendor negotiation and partnership strategies |

---

# 2. Data Structure Overview

### Data Sources

The analysis utilized transactional data from Premier Beverages' core operational systems, including:

| Data Source | Business Purpose |
|-------------|-------------------|
| Purchase Transactions | Records vendor procurement costs, quantities, and product costs |
| Sales Transactions | Tracks revenue generation, sales quantities, and realized prices |
| Inventory Records | Monitors stock levels, unsold capital, and turnover rates |
| Vendor Master Data | Maintains supplier relationships and performance history |
| Brand Information | Links products to brand-level performance metrics |

### Data Model

The underlying data structure connects transactional records across the procurement-to-sales lifecycle. Purchase transactions establish baseline costs and inventory quantities. Sales transactions capture revenue and actual selling prices. The relationship between purchase and sales quantities enables calculation of inventory turnover, gross profit, and profit margin metrics.

Data filtering was applied to enhance analytical reliability, excluding:
- Transactions with gross profit ≤ 0
- Transactions with profit margin ≤ 0
- Line items with total sales quantity = 0

### Key Metrics and KPIs

| KPI | Calculation Context | Measured Values |
|-----|---------------------|-------|
| Total Sales | Aggregated revenue across all transactions | $441.41M |
| Total Purchase | Aggregate procurement expenditure | $307.34M |
| Total Gross Profit | Sales minus purchase costs | $134.07M |
| Profit Margin | Gross profit / Total sales | 38.72% |
| Unsold Inventory Capital | Value of stock never sold | $2.71M |
| Stock Turnover | Sales quantity / Purchase quantity | Range: 0–274.5 |
| Vendor Purchase Contribution | Individual vendor purchase % of total | Top 10: 65.69% |
| Bulk Purchase Unit Cost | Average unit cost for large-volume orders | $10.78 |

---

# 3. Executive Summary

Premier Beverages generated **$441.41 million in total sales** with a **38.72% profit margin**, producing **$134.07 million in gross profit**. While these aggregate figures indicate a healthy business, detailed analysis reveals significant operational inefficiencies, concentration risks, and untapped profit optimization opportunities.

**Major Operational Findings:**

The company maintains **$2.71 million in unsold inventory capital**—products purchased but never sold. Stock turnover varies dramatically from 0 to 274.5, indicating that some inventory moves rapidly while other stock remains stagnant for extended periods.

**Key Supplier Insights:**

Vendor purchasing is highly concentrated, with the top 10 suppliers accounting for **65.69% of total purchases**. This concentration creates supply chain vulnerability. Bulk purchasing generates substantial cost advantages—vendors buying in large quantities receive **72% lower unit costs** ($10.78 vs. higher rates for small orders).

**Profitability Trends:**

A striking divergence exists between vendor performance models. Top-performing vendors (by sales volume) operate at a mean profit margin of **31.17%** (95% CI: 30.74%–31.61%). Low-performing vendors (by sales volume) actually maintain higher margins at **41.55%** (95% CI: 40.48%–42.62%), but struggle with sales volume. Statistical testing confirms these profitability differences are significant, indicating two fundamentally different business models.

**Most Significant Opportunities:**

- **198 brands** exhibit low sales volume with high profit margins, representing immediate promotional pricing opportunities
- Vendor diversification could reduce supply chain risk without sacrificing profitability
- Slow-moving inventory of $2.71M represents working capital that could be redeployed

---

# 4. Insights Deep Dive

## 4.1 Vendor Concentration and Supply Chain Risk

### Observation

The top 10 vendors contribute 65.69% of total purchases, while all remaining vendors collectively account for only 34.31%. Dashboard visualizations confirm DIAGEO NORTH, MARTIGNETTI, PERNOD RICA, JIM BEAM BR, and BACARDI USA as leading suppliers by both purchase volume and sales contribution.

### Business Impact

This concentration creates single-point-of-failure risk. Disruption with any top-tier vendor—whether due to pricing disputes, supply shortages, or logistical failures—would directly impact 5–11% of total procurement volume per vendor. Limited negotiating leverage with dominant suppliers may also constrain margin optimization.

### Supporting Evidence

- Top 10 vendors purchase contribution: 65.69%
- Remaining vendors: 34.31%
- Individual vendor purchase percentages range from 5.53% to 11.81% among top suppliers

---

## 4.2 Bulk Purchasing Cost Advantages

### Observation

Vendors committing to large purchase quantities receive unit costs **72% lower** than smaller orders. The bulk purchase average unit cost is $10.78, compared to significantly higher rates for low-volume procurement.

### Business Impact

This validates volume-based procurement strategies. Larger purchase commitments directly reduce cost of goods sold, expanding gross profit margins on every unit sold. The cost advantage creates competitive pricing flexibility while maintaining or improving profitability.

### Supporting Evidence

- Bulk purchase unit cost: $10.78
- Cost reduction vs. small orders: 72%
- Dashboard metric: Bulk pricing strategies encourage larger orders

---

## 4.3 Inventory Inefficiency and Unsold Capital

### Observation

Total unsold inventory capital is **$2.71 million**—products that were purchased but never sold to customers. Stock turnover ranges from 0 to 274.5, with some products showing zero sales despite being purchased. Negative gross profit values as low as -$52,002.78 indicate instances where products sold below purchase cost.

### Business Impact

Tied-up working capital reduces cash flow efficiency and increases storage carrying costs. Products with zero turnover represent direct financial losses. The wide turnover range suggests inconsistent inventory management practices across product categories and vendors.

### Supporting Evidence

- Unsold inventory capital: $2.71M
- Stock turnover range: 0 to 274.5
- Minimum gross profit: -$52,002.78
- Some products show zero sales despite purchase

---

## 4.4 Profit Margin Divergence Between Vendor Groups

### Observation

Statistical hypothesis testing rejected the null hypothesis of equal profit margins between top and low-performing vendors. Low-performing vendors (by sales volume) achieve a mean profit margin of **41.55%** (95% CI: 40.48%–42.62%), substantially higher than top-performing vendors at **31.17%** (95% CI: 30.74%–31.61%).

### Business Impact

Two distinct profitability models exist within the supplier base. Low-sales vendors achieve premium margins but lack volume. Top-sales vendors generate revenue but at compressed margins. Neither group has optimized the volume-margin trade-off. Opportunity exists to apply low-performing vendors' pricing strategies to high-volume products, or to increase volume for high-margin vendors.

### Supporting Evidence

| Vendor Group | Profit Margin Mean | 95% Confidence Interval |
|--------------|--------------------|--------------------------|
| Top-performing (by sales) | 31.17% | 30.74% – 31.61% |
| Low-performing (by sales) | 41.55% | 40.48% – 42.62% |

- Null hypothesis rejected: significant difference confirmed

---

## 4.5 Brands for Promotional Pricing Adjustments

### Observation

**198 brands** exhibit low total sales volume combined with high profit margins. Dashboard visualization shows a distinct cluster of brands where profit margin exceeds 50% despite sales under $2M. These brands are flagged as "Yes" for pricing adjustment opportunity.

### Business Impact

These brands represent under-monetized assets. Their high margins indicate pricing power or low cost structures, while low sales suggest insufficient market reach or promotional support. Targeted marketing or price optimization could increase volume without eroding profitability.

### Supporting Evidence

- 198 brands identified for pricing adjustment
- Dashboard: "Brands for promotional pricing adjustments" visualization
- High margin cluster above 50% profit margin with low sales volume

---

## 4.6 Correlation Analysis of Price and Profitability

### Observation

Purchase price shows weak correlation with total sales dollars (-0.012) and gross profit (-0.016). Profit margin has a negative correlation with total sales price (-0.179). Stock turnover shows weak negative correlation with gross profit (-0.038) and profit margin (-0.055).

### Business Impact

Higher purchase prices do not predict stronger sales revenue or profit—premium products do not automatically drive better financial outcomes. Increasing sales prices may actually reduce profit margins, suggesting price sensitivity or competitive pressures. Faster inventory turnover does not guarantee higher profitability, indicating that volume-focused strategies require margin discipline.

### Supporting Evidence

| Correlation Pair | Coefficient |
|------------------|--------------|
| Purchase price vs. total sales dollars | -0.012 |
| Purchase price vs. gross profit | -0.016 |
| Profit margin vs. total sales price | -0.179 |
| Stock turnover vs. gross profit | -0.038 |
| Stock turnover vs. profit margin | -0.055 |
| Total purchase quantity vs. total sales quantity | 0.999 |

---

# 5. Recommendations

## Recommendation 1: Launch Targeted Promotional Program for 198 High-Margin, Low-Sales Brands

**Objective:** Increase sales volume for the 198 brands with profit margins above 50% but low revenue contribution without eroding pricing power.

**Expected Business Impact:** Convert under-performing high-margin inventory into revenue-generating assets. A 20% volume increase across these brands at maintained margins would add approximately $X million in gross profit.

**Supporting Finding:** Dashboard identifies 198 brands flagged for pricing adjustment with high profit margins and low sales volume.

---

## Recommendation 2: Diversify Vendor Portfolio to Reduce Concentration Risk

**Objective:** Reduce top 10 vendor purchase concentration from 65.69% to below 50% within 12–18 months.

**Expected Business Impact:** Mitigates supply chain disruption risk, improves negotiating leverage, and creates competitive pressure on pricing. Each 5% reduction in top vendor concentration reduces single-supplier risk exposure by approximately $15M in purchasing volume.

**Supporting Finding:** Top 10 vendors control 65.69% of purchases. Individual vendors represent 5.53%–11.81% concentration.

---

## Recommendation 3: Expand Bulk Purchasing Program

**Objective:** Increase volume commitment procurement across eligible vendors to capture 72% unit cost savings on a larger percentage of total purchases.

**Expected Business Impact:** Reduce cost of goods sold by an estimated 10–15% on converted purchase volume. Every $1M shifted to bulk pricing saves approximately $720,000 in procurement costs.

**Supporting Finding:** Bulk purchase unit cost advantage of 72% ($10.78 vs. standard rates).

---

## Recommendation 4: Liquidate or Write Down Slow-Moving Inventory

**Objective:** Reduce $2.71M unsold inventory capital through clearance sales, vendor returns, or write-downs.

**Expected Business Impact:** Unlock $2.71M in working capital currently tied to non-performing stock. Reduce storage carrying costs by 15–25% of inventory value annually.

**Supporting Finding:** Total unsold inventory capital of $2.71M with stock turnover ranging down to zero.

---

## Recommendation 5: Replicate Low-Performing Vendor Margin Model Across Top Vendors

**Objective:** Apply the 41.55% profit margin model from low-sales vendors to high-volume vendor relationships.

**Expected Business Impact:** If top-performing vendors achieved even half the margin improvement (moving from 31.17% toward 41.55%), gross profit would increase by approximately $45–$60M annually.

**Supporting Finding:** Low-performing vendors maintain 41.55% mean profit margin vs. 31.17% for top-performing vendors. Statistical testing confirms distinct profitability models exist.

---

## Recommendation 6: Establish Vendor Performance Segmentation Framework

**Objective:** Create a two-dimensional vendor scorecard measuring both sales volume contribution and profit margin performance.

**Expected Business Impact:** Enables differentiated procurement strategies—negotiate margin improvements with high-volume vendors and volume growth with high-margin vendors. Prevents one-size-fits-all supplier management.

**Supporting Finding:** Weak correlation between stock turnover and profitability (-0.055) and between purchase price and gross profit (-0.016) indicates volume and margin are managed independently.

---

*Analysis conducted by Jorge Reyes. All data and metrics were calculeted using dummy data.*
