03 – Infrastructure, Security & Monitoring

What "Infrastructure as Code" (IaC) Means

Infrastructure as Code is the practice of managing and provisioning servers, networks, and cloud resources **using code** instead of manual configuration.  
It allows version control, repeatability, and automation of entire environments.

**Example Tools:** Terraform, CloudFormation.

**Benefits:**
- Consistency across environments.
- Easier rollback and audit.
- Faster provisioning and scaling.

---

What "Configuration Management" Means

Configuration Management ensures systems and software maintain a desired state over time.  
It automates installing packages, editing config files, managing users, and enforcing system policies.

**Example Tools:** Ansible, Puppet, Chef.

**Benefits:**
- Prevents configuration drift.
- Speeds up onboarding of new servers.
- Reduces human error.

---

What DevOps Engineers Monitor in Production

1. **System metrics:** CPU, memory, disk usage, network latency.  
2. **Application metrics:** request rates, response times, error percentages.  
3. **Logs:** application logs, server logs, and container logs for debugging.  
4. *(Bonus)* **Uptime & alerts:** monitoring SLOs and automated alerts on failures.

---

Key Security Practices in DevOps

1. **Secrets management:** using Vault or Azure Key Vault instead of hardcoding credentials.  
2. **Least privilege:** ensuring CI/CD pipelines and services have minimal access rights.  
3. **Vulnerability scanning:** scanning Docker images and dependencies automatically.  
4. **Secure pipelines:** using signed commits, HTTPS, and artifact integrity checks.
