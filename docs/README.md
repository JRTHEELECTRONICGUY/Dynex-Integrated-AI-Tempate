# Dynex AI Template

This template demonstrates a simple integration of FastAPI with a React-based frontend, intended for the Dynex marketplace.

# Dynex-Integrated AI Template

Contact Email: JRTheElectronicGuy@gmail.com

---

## Overview  
This project provides an AI-powered platform leveraging Dynex’s compute power. Users can perform advanced computations, access self-replicating code capabilities, and manage resources efficiently through cloud-integrated storage solutions like Google Drive.

---

## Key Features  
- Subscription Model with Tiers:  
  - Offers multiple usage tiers, each providing varying limits on API calls and compute cycles.  
  - Additional Premium Charges for requests exceeding tier limits.  

- Self-Replicating Logic:  
  - Code replication based on workload demand, ensuring high efficiency.  
  - Dynamically optimized resource management tied to compute usage.

- Integrated Resource Management:  
  - Users provide in-memory storage on their devices to reduce system overhead.  
  - Cloud options like Google Drive for session storage and retrieval.

- Enhanced Error Handling:  
  - Retry mechanisms in case of failures.  
  - User-friendly error messages for predictable failures.  
  - Monitoring tools for spotting potential API request overages.

---

## Pricing & Pay Structure  
Payment Exclusively in DXN Tokens

- Base Subscription Tiers:  
  - Basic Plan: 50 DXN/month – Limited API requests  
  - Pro Plan: 100 DXN/month – Higher API limits, access to premium services  
  - Enterprise Plan: 250 DXN/month – Maximum API limits + priority compute cycles

- Extra Charges:  
  - Exceeding API limits incurs additional DXN fees per request.  
  - Self-replicating workloads beyond limits will trigger incremental charges.  
  - Compute-heavy requests handled through Dynex’s marketplace compute quotas.

---

## System Architecture & Components  
- Front-end UI:  
  - Built with user-friendly forms to manage compute tasks and subscriptions.  
  - Login via Google for session storage integration.

- Backend Logic:  
  - Dynex-compatible code with self-replicating logic and efficient error handling.  
  - API request management with monitoring for request limits.

---

## Error Handling & Monitoring  
- Robust Retry Mechanism:  
  - Automatic retries up to three times on failures.  

- Failure Scenarios Handled:  
  - Invalid API requests  
  - Exceeded compute cycles  
  - Storage access failures

---

## Deployment Instructions  
1. Prepare Code Base:  
   - Ensure all dependencies are installed.  
   - Configure the Dynex API keys and set DXN as the only accepted currency.

2. Test Locally:  
   - Verify the subscription tiers and error handling functions work as expected.

3. Upload to GitHub:  
   - Create a public repository for your project.  
   - Include all documentation, dependencies, and source code.

4. Submit to Dynex Marketplace:  
   - Log in to your Dynex Marketplace account.  
   - Link the GitHub repository for automated testing.  
   - Ensure your pay structure aligns with Dynex’s marketplace policies.

---

## Code Structure  
- /src: Core logic, including self-replicating algorithms  
- /ui: Front-end interface files  
- /docs: Documentation for the entire project  
- /config: API keys, pricing settings, and dependencies  

---

## Future Enhancements  
- Add more premium services based on user feedback.  
- Refine UI for a more seamless user experience.  
- Implement real-time monitoring dashboards for API limits.

---

## License  
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Backend

- **FastAPI** for serving API requests.
- Start the server with:
  ```bash
  uvicorn backend.main:app --reload
  ```

## Frontend

- React setup with minimal HTML.
- Placeholder frontend, easily expandable for Dynex use cases.

## Usage

This template showcases a minimal but functional backend and frontend. Users can further expand it for their own needs.
