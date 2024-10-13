# Pricing Structure

Payment Method: DXN Tokens Only  

## 1. Subscription Tiers

| Plan        | Price (DXN/Month) | API Limit  | Included Compute Cycles |
|-----------------|----------------------|----------------|-----------------------------|
| Basic           | 50 DXN               | 100 requests   | 10 cycles                   |
| Pro             | 100 DXN              | 500 requests   | 50 cycles                   |
| Enterprise      | 250 DXN              | 2,000 requests | 200 cycles                  |

## 2. Additional Costs

If usage exceeds the limits within a subscription tier, the following fees will apply:

### API Request Overages
- 1 DXN per 10 additional API requests beyond the limit.
- Applied automatically once the limit is reached within the billing period.

### Compute Cycle Overages
- 5 DXN per additional compute cycle beyond the included cycles.
- Compute cycles represent heavy workloads (e.g., data analysis, AI model inference).

### Self-Replicating Workloads
- 10 DXN per replicated instance for high-demand workloads that spawn additional processes.
- Ensures resource usage remains sustainable within the Dynex ecosystem.

## 3. Storage Management Costs
- In-Memory Cache: Users provide their own memory storage to reduce infrastructure costs.
- Google Drive Integration (Optional):
  - 5 DXN per session to link and access Google Drive for data storage.
  - Sessions persist for 24 hours.

## 4. Error Handling & Auto-Retries
- 3 DXN per failed request after three retry attempts.
- Ensures the platform covers any unexpected compute spikes or failed operations.
